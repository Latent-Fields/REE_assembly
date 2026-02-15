# Documentation Refactoring Changelog

**Claim Type:** implementation_note  
**Scope:** Documentation change history  
**Depends On:** None  
**Status:** stable  
**Claim ID:** IMPL-014
<a id="impl-014"></a>

## 2026-02-15: Processed Commit-Gating Refresh Thought

### Overview

Processed the refreshed thought on commit gating, pre/post-commit error separation, and expanded control-plane axes,
and promoted its unresolved parts into explicit implementation-gap contracts.

### What Changed

- Updated E3 canonical spec:
  - `docs/architecture/e3.md`
  - added explicit open implementation-gap contract for MECH-061/MECH-062:
    - commit-token wire format/scope
    - cross-gate arbitration policy
    - post-commit credit-assignment interface
    - responsibility-locus storage contract
- Updated control-plane canonical spec:
  - `docs/architecture/control_plane.md`
  - added phenomenology-aligned diagnostic profile for "focused but initiation-suppressed" regimes
- Marked thought as processed:
  - `docs/thoughts/2026-02-15_basal_ganglia_commit_gating_control_plane_axes_refresh.md`

---

## 2026-02-15: Frictionless Task Inbox Sync for Governance Carryover

### Overview

Added a markdown checklist inbox that automatically syncs into manual carryover tracking so tasks are captured quickly
and disappear from agenda carryover as soon as they are checked done.

### What Changed

- Added task inbox sync script:
  - `evidence/planning/scripts/sync_task_inbox.py`
  - parses `evidence/planning/task_inbox.md` checklist items
  - open (`- [ ]`) items are created/reopened in `manual_carryover_items.v1.json`
  - done (`- [x]`) items are marked `status=done` in carryover
  - done checkbox lines are pruned from inbox by default after sync (`--no-prune-completed` opt-out)
  - stable matching uses source refs (`task_inbox:<sha1>`) derived from normalized task text
- Added default inbox file:
  - `evidence/planning/task_inbox.md`
- Integrated task inbox sync into governance cycle:
  - `evidence/planning/scripts/run_governance_cycle.py`
  - new flags:
    - `--skip-task-inbox-sync`
    - `--task-inbox-dry-run`
- Updated planning docs:
  - `evidence/planning/README.md`
  - `evidence/planning/LOCAL_CADENCE_AUTOMATION.md`

## 2026-02-14: Automated Adjudication Cascade Application

### Overview

Added post-decision automation that applies adjudication outcomes to the claim registry and reopens dependent claims
when structural outcomes (`adopt_jepa_structure` / `retire_ree_claim`) are selected.

### What Changed

- Added adjudication cascade script:
  - `evidence/planning/scripts/apply_adjudication_cascade.py`
  - reads latest decision-log entries by claim
  - applies configured outcome tokens for `decision_status=applied`
  - updates `docs/claims/claims.yaml` adjudication/cascade fields
  - emits:
    - `evidence/decisions/adjudication_cascade_state.v1.json`
    - `evidence/planning/ADJUDICATION_CASCADE_PATCH_QUEUE.md`
- Integrated cascade step into governance cycle:
  - `evidence/planning/scripts/run_governance_cycle.py`
  - new step: `adjudication_cascade` (enabled by default)
  - new flags:
    - `--skip-adjudication-cascade`
    - `--adjudication-cascade-statuses`
    - `--adjudication-cascade-dry-run`
  - agenda now includes `Adjudication Cascade` checkpoint and action counts.
- Updated runbooks:
  - `evidence/planning/README.md`
  - `evidence/planning/LOCAL_CADENCE_AUTOMATION.md`
  - `evidence/decisions/README.md`

## 2026-02-14: External-Precedence Governance Policy (JEPA vs REE)

### Overview

Added an explicit governance policy that allows REE claim replacement when matched JEPA evidence is stronger, with
cascade handling and anti-lock-in safeguards.

### What Changed

- Extended planning criteria with executable adjudication policy:
  - `evidence/planning/planning_criteria.v1.yaml`
  - added `model_adjudication` section:
    - allowed outcomes: `retain_ree`, `hybridize`, `adopt_jepa_structure`, `retire_ree_claim`
    - cascade policy for dependency reopen on structural replacement
    - temporary override mode for JEPA-internal proxy routing with provenance/calibration/rollback requirements
    - anti-lock-in gate
  - added thresholds for external-precedence detection.
- Updated planning generation to propagate adjudication/cascade context into backlog and architecture gap outputs:
  - `evidence/experiments/scripts/build_experiment_indexes.py`
  - external-precedence and anti-lock-in signals are now computed and surfaced in generated planning artifacts.
- Updated governance agenda builder to report model adjudication checkpoint:
  - `evidence/planning/scripts/run_governance_cycle.py`
  - includes candidate claims, allowed outcomes, cascade policy, and override mode in agenda outputs.
- Added claim-level lifecycle/adjudication metadata for core JEPA-sensitive claims:
  - `docs/claims/claims.yaml`
  - updated `MECH-056`, `MECH-058`, `MECH-059`, `MECH-060`, and `IMPL-022`.

## 2026-02-14: JEPA Control-Signal Mapping Matrix and Proxy Contract

### Overview

Hardened JEPA integration wording and interfaces so REE control-plane routing can use internal JEPA proxies without
collapsing control ownership into the substrate layer.

### What Changed

- Updated JEPA integration contract with explicit JEPA↔REE control signal mapping matrix:
  - `docs/architecture/jepa_e1e2_integration_contract.md`
  - clarified that precision is not guaranteed as an explicit calibrated JEPA output channel
  - added execution table for `MECH-056`, `MECH-058`, `MECH-059`, `MECH-060`
  - added proxy-bank declaration contract and explicit provenance/calibration/separability/ablation checks
- Updated v2 substrate spec with JEPA control-proxy profile and hard-fail thresholds:
  - `docs/architecture/ree_v2_spec.md`
  - added `jepa_control_proxy_ablation` profile
  - added proxy metrics and readiness thresholds (`proxy_bank_coverage_rate`, calibration ECE, residual separability, ablation utility)
- Extended adapter signal schema and producer contract for proxy-bank metadata:
  - `evidence/experiments/schemas/v1/jepa_adapter_signals.v1.json`
  - `evidence/experiments/INTERFACE_CONTRACT.md`
  - proxy declarations are optional in base v1, but conditional metrics are required when `proxy_bank` is present

## 2026-02-14: Connectome Literature Pull Implementation

### Overview

Added a generated connectome-oriented literature pull queue to turn architecture pressure signals into
concrete, claim-scoped evidence pulls with source-preserving translation and confidence decomposition requirements.

### What Changed

- Added connectome pull generator:
  - `evidence/planning/scripts/build_connectome_literature_pull.py`
  - outputs:
    - `evidence/planning/connectome_literature_pull.v1.json`
    - `evidence/planning/CONNECTOME_LITERATURE_PULL.md`
- Integrated connectome pull generation into governance cycle:
  - `evidence/planning/scripts/run_governance_cycle.py`
  - new step: `connectome_pull`
  - new agenda checkpoint: `Connectome Literature Pull`
- Extended literature contract and schema for source-preserving translation and confidence decomposition:
  - `evidence/literature/INTERFACE_CONTRACT.md`
  - `evidence/literature/schemas/v1/literature_evidence.schema.json`
  - new optional record fields:
    - `mapping` (`source_claim_statement`, `ree_translation`, `mapping_caveat`, optional `source_context`)
    - `confidence_components` (`source_quality`, `mapping_fidelity`, `transfer_risk`, optional `notes`)
- Added planning schema for connectome pull artifact:
  - `evidence/planning/schemas/v1/connectome_literature_pull.schema.json`

## 2026-02-14: MECH-059 Terminology Standardization

### Overview

Standardized `MECH-059` language to avoid ambiguity between uncertainty and precision by using:
**confidence channel (uncertainty-derived precision)**, explicitly separate from residual prediction error.

### What Changed

- Updated canonical mechanism wording:
  - `docs/architecture/agency_responsibility_flow.md#mech-059`
- Updated JEPA contract wording:
  - `docs/architecture/jepa_e1e2_integration_contract.md`
- Updated claim metadata and index label:
  - `docs/claims/claims.yaml`
  - `docs/claims/claim_index.md`
- Updated v2 planning/spec references:
  - `docs/architecture/ree_v2_spec.md`
  - `docs/architecture/ree_v2_repo_bootstrap_spec.md`
- Updated governance decision packet phrasing:
  - `evidence/decisions/decision_packet_v3_conflicts_2026-02-14.md`

## 2026-02-14: Structure Review Dossier Protocol

### Overview

Added a generated human-decision packet for architecture pressure claims so governance can review
claim context, REE fit, evidence mix, alternatives, and inspiration options before deciding structural changes.

### What Changed

- Added structure review dossier generator:
  - `evidence/planning/scripts/build_structure_review_dossiers.py`
  - generates per-claim dossiers from `architecture_gap_register.v1.json` and `claim_evidence.v1.json`
  - includes plain-English claim description followed by plain-English REE whole-system fit description
  - includes evidence-mix interpretation, alternative hypotheses with confidence estimates, source wording vs REE translation, and left-field suggestions
- Added generated dossier outputs:
  - `evidence/planning/structure_review/<YYYY-MM-DD>/<CLAIM_ID>/DOSSIER.md`
  - `evidence/planning/structure_review/<YYYY-MM-DD>/<CLAIM_ID>/dossier.v1.json`
  - `evidence/planning/structure_review/latest/INDEX.md`
  - `evidence/planning/structure_review/latest/structure_review_report.v1.json`
- Integrated dossier generation into governance cycle:
  - `evidence/planning/scripts/run_governance_cycle.py`
  - new step: `structure_review`
  - new agenda checkpoint: `Structure Dossiers`
- Extended planning thresholds to support soft structural trigger logic:
  - `evidence/planning/planning_criteria.v1.yaml`
  - trigger outcome is `consider_new_structure` (advisory), not automatic refactor.

## 2026-02-14: High-Priority Literature Dispatch Pack

### Overview

Added an explicit dispatch bundle for the current high-priority literature backlog so governance-critical claims can be
worked in a single focused evidence cycle.

### What Changed

- Added literature dispatch pack:
  - `evidence/planning/DISPATCH_LITERATURE_HIGH_PRIORITY_2026-02-14.md`
- Includes:
  - proposal queue for `LIT-0005`, `LIT-0008`, `LIT-0013`, `LIT-0016`, `LIT-0018`, `LIT-0020`, `LIT-0022`
  - acceptance checks and a copy/paste execution prompt for `REE_assembly`

## 2026-02-14: REE-v2 Cutover Adjudication Gate

### Overview

Added a reusable cutover readiness checker that allows justified `ree-v2` vs `ree-v1-minimal` direction divergence
when explicit adjudication criteria pass, instead of treating all mismatches as automatic failures.

### What Changed

- Added cutover checker script:
  - `evidence/planning/scripts/check_ree_v2_cutover_readiness.py`
  - evaluates latest producer handoff snapshots and latest ingestion-cycle reports
  - replaces strict overlap gate with `overlap_sanity_adjudicated_or_resolved`
  - enforces per-claim adjudication checks:
    - matched protocol evidence (seeds/conditions/schema version set)
    - ree-v2 CI pass status
    - metric improvement rule (`>=3` claim-critical metrics improved on `>=2/3` seeds)
    - no `contract:*` drift signatures
    - no unaddressed `P0` falsification for claim in latest lab handoff
    - governance note presence with rationale and rollback trigger
- Updated planning readme with cutover command:
  - `evidence/planning/README.md`

## 2026-02-14: Cross-Version Hook Surface Framework

### Overview

Added a versioned hook framework so v2 can expose forward-compatible extension points for v3/v4 without repeated
interface churn.

### What Changed

- Added hook contract document:
  - `docs/architecture/hook_surface_contract.md#impl-025`
- Added initial hook registry:
  - `docs/architecture/hook_registry.v1.json`
  - includes `v2_required`, `v3_planned`, and `v4_plus_reserved` tiers
- Updated v2 spec to consume hook framework:
  - `docs/architecture/ree_v2_spec.md#impl-023`
- Added claim/index/mapping entries:
  - `docs/claims/claims.yaml` (`IMPL-025`)
  - `docs/claims/claim_index.md` (`IMPL-025`)
  - `docs/claims/subsystem_map.yaml`

## 2026-02-14: REE-v2 JEPA Source and Cloud Compute Planning

### Overview

Extended the REE-v2 bootstrap plan to explicitly require JEPA source provenance locking and a local-vs-cloud execution
policy suitable for laptop-constrained development environments.

### What Changed

- Expanded REE-v2 bootstrap spec with:
  - JEPA source acquisition/provenance contract (`third_party/jepa_sources.lock.v1.json`)
  - local-vs-cloud offload gate and remote export/import gate
  - hobby-mode runtime placement baseline updated to `360m/360m` for `macbook_air_m2_2022`
  - local hardware options/cost visibility gate (`docs/ops/local_compute_options.md`)
  - explicit hobby-mode buy/hold thresholds in EUR for structured decisions
  - migration stage updates and cutover acceptance updates
  - `docs/architecture/ree_v2_repo_bootstrap_spec.md`
- Updated REE-v2 bootstrap dispatch prompt to include:
  - MacBook Air M2 local constraints
  - required remote execution scripts and dry-run acceptance checks
  - JEPA provenance fields required in `manifest.scenario`
  - required local compute options/cost sheet deliverable and output table
  - `evidence/planning/DISPATCH_REE_V2_BOOTSTRAP.md`
- Extended weekly handoff template and policy to report compute placement:
  - `execution_mode`, `compute_backend`, `runtime_minutes`
  - remote export/import CI gate status
  - ree-v2 local compute options watch section for buy/hold decisions
  - `evidence/planning/WEEKLY_HANDOFF_TEMPLATE.md`
  - `evidence/experiments/CROSS_REPO_SYNC_POLICY.md`
  - `evidence/planning/DISPATCH_WEEKLY_HANDOFF_FORMAT_UPDATE_2026-02-14.md`
- Added structured operator checklist for spare-time workflow:
  - `evidence/planning/HOBBY_OPERATOR_PLAYBOOK.md`

## 2026-02-14: Local Cadence Automation Scripts

### Overview

Added local-scheduler automation for weekly producer handoff sync/import and outbound dispatch generation.

### What Changed

- Added cadence automation config:
  - `evidence/planning/cadence_automation.v1.json`
- Added handoff sync/import script:
  - `evidence/planning/scripts/sync_weekly_handoffs.py`
  - supports day-based repo selection, handoff validation, run-pack import, and optional ingestion/governance steps
- Added weekly dispatch emission script:
  - `evidence/planning/scripts/emit_weekly_dispatches.py`
  - builds per-repo dispatch markdown bundles from `experiment_proposals.v1.json`
- Added local scheduling runbook:
  - `evidence/planning/LOCAL_CADENCE_AUTOMATION.md`
- Updated planning docs for discoverability and handoff-path guidance:
  - `evidence/planning/README.md`
  - `evidence/planning/WEEKLY_HANDOFF_TEMPLATE.md`
  - `evidence/experiments/CROSS_REPO_SYNC_POLICY.md`

## 2026-02-14: Weekly Cross-Repo Handoff Standardization

### Overview

Standardized weekly producer handoff format across qualification, stress, and parity lanes and added dispatch prompts
to upgrade producer repos to the shared format.

### What Changed

- Updated cross-repo sync policy to include all producer repos and staggered weekly cadence:
  - `evidence/experiments/CROSS_REPO_SYNC_POLICY.md`
- Added shared weekly handoff template:
  - `evidence/planning/WEEKLY_HANDOFF_TEMPLATE.md`
- Added copy/paste dispatch bundle for producer format upgrades:
  - `evidence/planning/DISPATCH_WEEKLY_HANDOFF_FORMAT_UPDATE_2026-02-14.md`
- Updated planning README:
  - `evidence/planning/README.md`

## 2026-02-14: Qualification Lane Ownership Update (`ree-v2`)

### Overview

Updated v2 planning docs so `ree-v2` (not `ree-v1-minimal`) is the intended qualification lane, with `ree-v1-minimal`
retained as a transitional baseline during migration.

### What Changed

- Updated qualification-lane wording in:
  - `docs/architecture/ree_v2_spec.md#impl-023`
- Updated repository-role framing in:
  - `docs/roadmap.md#impl-008`

## 2026-02-14: REE-v2 Spec Expansion (Implementation Detail Pass)

### Overview

Expanded the v2 spec from framing-level draft into an implementation-ready contract with explicit module layout,
configuration requirements, qualification profiles, milestones, and go/no-go criteria.

### What Changed

- Expanded:
  - `docs/architecture/ree_v2_spec.md#impl-023`
- Added concrete sections for:
  - implementation objectives,
  - reference module layout,
  - interface detail and configuration contract,
  - qualification profiles (`MECH-058/059/060`),
  - failure thresholds and milestone gates (`M0`-`M4`),
  - acceptance checklist for v2 completion.

## 2026-02-14: v2 JEPA-First Wording Policy

### Overview

Added explicit v2 terminology policy so docs and user-facing interactions use JEPA-first language with inline REE
translation, while keeping machine contracts stable.

### What Changed

- Added policy doc:
  - `docs/notes/jepa_language_policy.md#impl-024`
- Wired v2 spec to policy:
  - `docs/architecture/ree_v2_spec.md#impl-023`
- Added operating-procedure rule:
  - `docs/README.md#impl-013`
- Added glossary policy note:
  - `docs/glossary.md#impl-020`
- Added claim/index/mapping entries:
  - `docs/claims/claims.yaml` (`IMPL-024`)
  - `docs/claims/claim_index.md` (`IMPL-024`)
  - `docs/claims/subsystem_map.yaml`

## 2026-02-14: Roadmap Refresh and REE-v2 Spec Draft

### Overview

Refreshed the roadmap to reflect current repository roles and moved program framing to a substrate-first v2 followed by
control-completion v3. Added a dedicated v2 implementation spec document.

### What Changed

- Rewrote roadmap:
  - `docs/roadmap.md#impl-008`
  - reframed v1 as qualification harness outcome
  - defined v2 as JEPA-aligned substrate phase
  - defined v3 as control-plane/hippocampal/E3 completion phase
- Added v2 spec:
  - `docs/architecture/ree_v2_spec.md#impl-023`
- Added claims/index mapping for v2 spec:
  - `docs/claims/claims.yaml` (`IMPL-023`)
  - `docs/claims/claim_index.md` (`IMPL-023`)
  - `docs/claims/subsystem_map.yaml` (JEPA-REE alignment mapping includes v2 spec)
- Added literature dispatch pack for v3-critical evidence:
  - `evidence/planning/DISPATCH_LIT_V3_HIPPO_PFC_JEPA.md`

## 2026-02-13: Invariant Rewording for Consequence Persistence (INV-004/INV-006)

### Overview

Reworded persistence invariants to be mechanism-agnostic now that consequence retention is distributed across more
specific architecture claims (including but not limited to residue geometry).

### What Changed

- Updated invariant language in:
  - `docs/invariants.md`
  - `INV-004` now: post-commit consequence traces are persistent
  - `INV-006` now: post-commit consequence traces cannot be erased
- Updated claim registry/index wording:
  - `docs/claims/claims.yaml` (subjects for `INV-004`, `INV-006`)
  - `docs/claims/claim_index.md`
- Updated dependency wording in:
  - `docs/architecture/residue_geometry.md`

## 2026-02-13: Targeted Literature Entries for MECH-058/059/060

### Overview

Added first-pass literature triangulation entries for new JEPA follow-on claims and refreshed evidence indexes.

### What Changed

- Added literature evidence entries:
  - `evidence/literature/targeted_review_mech_058/entries/2026-02-13_mech058_ijepa_target_encoder_anchor/record.json`
  - `evidence/literature/targeted_review_mech_058/entries/2026-02-13_mech058_ijepa_target_encoder_anchor/summary.md`
  - `evidence/literature/targeted_review_mech_059/entries/2026-02-13_mech059_vjvcr_uncertainty_channeling/record.json`
  - `evidence/literature/targeted_review_mech_059/entries/2026-02-13_mech059_vjvcr_uncertainty_channeling/summary.md`
  - `evidence/literature/targeted_review_mech_060/entries/2026-02-13_mech060_vjepa2_dual_loss_channels/record.json`
  - `evidence/literature/targeted_review_mech_060/entries/2026-02-13_mech060_vjepa2_dual_loss_channels/summary.md`
- Regenerated evidence outputs via:
  - `python3 evidence/experiments/scripts/build_experiment_indexes.py`

## 2026-02-13: Dispatch Bundle for MECH-058/059/060

### Overview

Added a focused cross-repo dispatch bundle for first-pass evidence generation on the new JEPA follow-on mechanism
claims.

### What Changed

- Added dispatch bundle with copy/paste prompts:
  - `evidence/planning/DISPATCH_JEPA_MECH_058_060.md`
- Updated planning README to document curated dispatch files:
  - `evidence/planning/README.md`

## 2026-02-13: JEPA Follow-On Claim Stubs (MECH-058/059/060, Q-013/014)

### Overview

Added draft claim stubs capturing JEPA-driven follow-on mechanisms and open questions for governance/evidence routing.

### What Changed

- Added mechanism stubs in:
  - `docs/architecture/agency_responsibility_flow.md`
  - `MECH-058` slow target-anchor timescale separation
  - `MECH-059` latent uncertainty stream separation
  - `MECH-060` pre-commit vs post-commit dual error channels
- Added open questions in:
  - `docs/architecture/agency_responsibility_flow.md`
  - `Q-013` deterministic vs stochastic uncertainty calibration
  - `Q-014` invariance blind-spot risk for ethical attribution
- Added claim registry and index entries:
  - `docs/claims/claims.yaml`
  - `docs/claims/claim_index.md`

## 2026-02-13: Cross-Repo Contract Sync Policy

### Overview

Added a minimal lockstep policy so producer repos can stay aligned with REE_assembly experiment contract schemas and
fail fast on drift.

### What Changed

- Added policy file:
  - `evidence/experiments/CROSS_REPO_SYNC_POLICY.md`
- Updated evidence README index:
  - `evidence/experiments/README.md`

## 2026-02-13: JEPA Adapter Signals Schema + Ingestion Validation

### Overview

Added a machine-readable JEPA adapter signal contract and wired ingestion to validate declared adapter artifacts so
contract drift is surfaced automatically as FAIL evidence.

### What Changed

- Added schema:
  - `evidence/experiments/schemas/v1/jepa_adapter_signals.v1.json`
- Extended manifest artifact schema:
  - `evidence/experiments/schemas/v1/manifest.schema.json` (`artifacts.adapter_signals_path`)
- Extended ingestion:
  - `evidence/experiments/scripts/build_experiment_indexes.py`
  - validates adapter signal files when declared in manifest
  - marks invalid/missing adapter artifacts as FAIL with `contract:jepa_adapter_signals_*`
  - shows adapter contract status in per-experiment indexes
- Updated experiment contract docs:
  - `evidence/experiments/INTERFACE_CONTRACT.md`
  - `evidence/experiments/README.md`
- Added example adapter artifacts in dummy run packs:
  - `evidence/experiments/trajectory_integrity/runs/*/jepa_adapter_signals.v1.json`

## 2026-02-13: Hybrid JEPA to REE Diagram Spec + JEPA Literature Pull

### Overview

Added a canonical hybrid-diagram contract so JEPA↔REE alignment can be discussed with consistent structure, then
ingested targeted JEPA-paper evidence into the literature pipeline for MECH-057/Q-012.

### What Changed

- Added hybrid diagram contract:
  - `docs/architecture/jepa_ree_hybrid_diagram_spec.md#impl-021`
- Added JEPA-as-E1/E2 integration contract:
  - `docs/architecture/jepa_e1e2_integration_contract.md#impl-022`
- Added claim registry/index entries:
  - `docs/claims/claims.yaml` (`IMPL-021`, `IMPL-022`)
  - `docs/claims/claim_index.md` (`IMPL-021`, `IMPL-022`)
  - `docs/claims/subsystem_map.yaml` (new `JEPA-REE Hybrid Alignment` mapping)
- Added targeted JEPA literature entries:
  - `evidence/literature/targeted_review_mech_057/entries/*`
- Refreshed evidence indexes/matrices using:
  - `evidence/experiments/scripts/build_experiment_indexes.py`

## 2026-02-13: IMPL-022 Signal-Contract Tightening (JEPA Native Streams)

### Overview

Tightened the JEPA integration contract so adapter outputs are explicit about what is native to JEPA versus what must
be derived for REE precision-control usage.

### What Changed

- Updated `docs/architecture/jepa_e1e2_integration_contract.md#impl-022` with:
  - JEPA-native signal map table (`z`, `z_hat`, residuals, uncertainty, trace fields),
  - signed-PE boundary rule (adapter emits unsigned substrate streams only),
  - additional required knobs for residual/uncertainty export mode,
  - extra metrics/checks for uncertainty provenance and precision-input completeness.

## 2026-02-13: Thought Processing - Formal JEPA to REE Alignment Glossary

### Overview

Processed a dedicated JEPA↔REE terminology alignment thought into a formal interoperability glossary section.
This pass is documentation-level alignment: it does not claim equivalence of objectives, only consistent mapping between
representation/prediction/control terms across both frames.

### What Changed

- Expanded and formalized JEPA↔REE mapping in:
  - `docs/glossary.md#impl-020`
- Added claim registry entry:
  - `docs/claims/claims.yaml` (`IMPL-020`)
- Added claim index entry:
  - `docs/claims/claim_index.md` (`IMPL-020`)
- Marked thought as processed with canonical links:
  - `docs/thoughts/2026-02-13_jepa_ree_formal_alignment_glossary.md`

## 2026-02-13: Thought Processing - JEPA to REE Convergence

### Overview

Processed the JEPA↔REE convergence thought into a new candidate mechanism and an explicit falsifiability question.
The integration captures a minimal architectural claim (latent predictive geometry plus control completion pressure)
without committing to the strong claim as settled.

### What Changed

- Added mechanism `MECH-057` in:
  - `docs/architecture/agency_responsibility_flow.md#mech-057`
- Added open question `Q-012` in:
  - `docs/architecture/agency_responsibility_flow.md#q-012`
- Added JEPA↔REE vocabulary bridge in:
  - `docs/glossary.md`
- Added claim registry entries:
  - `docs/claims/claims.yaml` (`MECH-057`, `Q-012`)
- Added claim index entries:
  - `docs/claims/claim_index.md` (`MECH-057`, `Q-012`)
- Marked thought as processed with canonical links:
  - `docs/thoughts/2026-02-13_LeCun_developed_lots_of_REE.md`

## 2026-02-13: Thought Processing - Self-First, Social-Later Roadmap Heuristic

### Overview

Processed the developmental-roadmap thought and promoted it as a governance/testing heuristic without converting it
into a new architectural commitment.

### What Changed

- Added implementation note `IMPL-019` in:
  - `docs/architecture/developmental_curriculum.md#impl-019`
- Added claim registry entry:
  - `docs/claims/claims.yaml` (`IMPL-019`)
- Added claim index entry:
  - `docs/claims/claim_index.md` (`IMPL-019`)
- Marked thought as processed with canonical links:
  - `docs/thoughts/DEV-ROADMAP-SELF-FIRST-SOCIAL-LATER.md`

## 2026-02-13: Claims Explorer Governance Dashboard Tab

### Overview

Extended the HTML claims explorer so it can act as a governance dashboard for the new evidence loop.

### What Changed

- Updated `docs/claims/explorer.html` with a new **Governance** view tab.
- Added dashboard rendering for:
  - governance cycle summary cards,
  - thought-intake queue,
  - conflict queue,
  - decision queue,
  - high-priority backlog and proposal snapshots,
  - dispatch-by-target-repo,
  - and maintenance flags/warnings.
- Added staleness indicator based on `evidence/planning/governance_agenda.v1.json`.
- Added copy-command helpers (manual CLI flow):
  - run governance cycle,
  - strict thought-gate cycle,
  - record-decision template command.

## 2026-02-13: Governance Cycle Orchestrator

### Overview

Added a single helper that runs non-decision upkeep steps and emits a structured conversation agenda.

### What Changed

- Added script:
  - `evidence/planning/scripts/run_governance_cycle.py`
- Script executes:
  - `docs/thoughts/scripts/thought_sweep.py`
  - `evidence/experiments/scripts/build_experiment_indexes.py`
- Added generated agenda outputs:
  - `evidence/planning/governance_agenda.v1.json`
  - `evidence/planning/GOVERNANCE_AGENDA.md`
- Updated planning docs:
  - `evidence/planning/README.md`

## 2026-02-13: Deterministic Thought Sweep Helper

### Overview

Added a small utility to make thought-intake sweeps deterministic and repeatable.

### What Changed

- Added script:
  - `docs/thoughts/scripts/thought_sweep.py`
- Added generated sweep outputs:
  - `docs/thoughts/thought_sweep.v1.json`
  - `docs/thoughts/SWEEP_REPORT.md`
- Updated usage guidance in:
  - `docs/thoughts/README.md`

## 2026-02-13: Human-in-the-Loop Decision Queue, Confidence Channels, and Literature Merge

### Overview

Extended the evidence subsystem so promotion/demotion decisions are surfaced as explicit review items, claim confidence
is channelized by source, and literature evidence can be ingested alongside experiments.

### What Changed

- Added decision thresholds file `evidence/experiments/decision_criteria.v1.yaml`.
- Added persistent decision governance files:
  - `evidence/decisions/decision_log.v1.jsonl` (append-only)
  - `evidence/decisions/decision_state.v1.json` (generated snapshot)
  - `evidence/decisions/schemas/v1/decision_log_entry.schema.json`
- Extended ingestion script `evidence/experiments/scripts/build_experiment_indexes.py` to:
  - merge `evidence/literature/**/entries/**/record.json` with experiment evidence,
  - compute `experimental_confidence`, `literature_confidence`, and `overall_confidence`,
  - generate `evidence/experiments/conflicts.md`,
  - generate `evidence/experiments/promotion_demotion_recommendations.md` with human decision status,
  - read decision history from `evidence/decisions/decision_log.v1.jsonl`,
  - and generate decision state snapshot `evidence/decisions/decision_state.v1.json`,
  - and refresh `evidence/literature/INDEX.md`.
- Added decision logging helper script:
  - `evidence/experiments/scripts/record_decision.py`
- Added planning subsystem and generated loop outputs:
  - `evidence/planning/planning_criteria.v1.yaml`
  - `evidence/planning/evidence_backlog.v1.json`
  - `evidence/planning/experiment_proposals.v1.json`
  - `evidence/planning/INDEX.md`
  - `evidence/planning/schemas/v1/evidence_backlog.schema.json`
  - `evidence/planning/schemas/v1/experiment_proposals.schema.json`
- Extended ingestion script to generate planning backlog/proposals directly from matrix + conflicts + decision log.
- Extended claim-evidence schema `evidence/experiments/schemas/v1/claim_evidence.schema.json` with:
  - `source_type` split (`experimental` vs `literature`),
  - entry-level confidence fields,
  - claim-level confidence channels and source counts.
- Added literature subsystem docs and schema:
  - `evidence/literature/README.md`
  - `evidence/literature/INTERFACE_CONTRACT.md`
  - `evidence/literature/schemas/v1/literature_evidence.schema.json`
- Added example literature evidence record:
  - `evidence/literature/neuro_pe_habenula_da/entries/2026-02-13_habenula_da_signed_pe_review/record.json`
  - `evidence/literature/neuro_pe_habenula_da/entries/2026-02-13_habenula_da_signed_pe_review/summary.md`

## 2026-02-13: Experimental Evidence Ingestion Pipeline

### Overview

Added a repository-level experiment ingestion subsystem so external implementation runs can be indexed in REE_assembly
and translated into design-facing implications and TODOs.

### What Changed

- Added `evidence/experiments/` with a versioned Experiment Pack contract:
  - `manifest.json`, `metrics.json`, `summary.md`, optional `traces/` and `media/`.
- Added schemas in `evidence/experiments/schemas/v1/` for manifest and metrics files.
- Added claim-evidence matrix schema in `evidence/experiments/schemas/v1/claim_evidence.schema.json`.
- Added versioned stop criteria in `evidence/experiments/stop_criteria.v1.yaml`.
- Added ingestion/index script `evidence/experiments/scripts/build_experiment_indexes.py` (standard library only) that:
  - scans `evidence/experiments/**/runs/**/manifest.json`,
  - flags FAIL runs using manifest status plus stop-criteria checks,
  - generates per-experiment and top-level indexes,
  - computes key metric deltas across runs,
  - populates `evidence/experiments/claim_evidence.v1.json` from `claim_ids_tested`,
  - auto-updates design implications in experiment templates,
  - and refreshes a failure-driven TODO queue.
- Added strict producer-facing interface contract in `evidence/experiments/INTERFACE_CONTRACT.md`.
- Added usage/readme documentation in `evidence/experiments/README.md`.
- Added example experiment type `trajectory_integrity` with dummy PASS/FAIL runs demonstrating criteria-triggered failure indexing.

## 2026-02-12: Consistency Sweep (Dependencies, Conflicts, Open Questions)

### Overview

Ran a repo-wide documentation consistency pass to tighten dependency symmetry, conflict tracking coverage, and
open-question navigation.

### What Changed

- Added missing conflict records:
  - `docs/conflicts/valence_vectors_vs_mu_kappa_overlays.md`
  - `docs/conflicts/care_override_vs_other_harm_veto.md`
  - `docs/conflicts/rollout_entropy_floor_vs_residue_persistence.md`
- Added missing resolution note and backlink for the previously resolved ethics conflict:
  - `docs/conflicts/resolutions/2026-02-08_ethics-module-vs-cost-term.md`
  - `docs/conflicts/ethics_module_vs_cost_term.md`
- Updated `docs/conflicts/README.md` to index all active conflicts and map Q-008/Q-009/Q-011 to their trackers.
- Added tracked-conflict links in open-question sections of:
  - `docs/architecture/control_plane.md` (Q-008)
  - `docs/architecture/social.md` (Q-009)
  - `docs/architecture/hippocampal_systems.md` (Q-011)
- Updated `docs/claims/claim_index.md` for status symmetry:
  - Marked MECH-008 and MECH-020 as legacy in summaries.
  - Added conflict-tracker references to Q-008/Q-009/Q-011 index entries.
- Updated `docs/claims/claims.yaml` so IMPL-017 depends on Q-008/Q-009/Q-011 and cites new conflict sources.
- Logged an explicit open-question registry sweep in `docs/notes/synthesis_passes.md` (Q-001 through Q-011 coverage/triage).

## 2026-02-12: Justification Invariants and Operational Control-State Hooks

### Overview

Converted prior discussion points into explicit architecture contracts: justification-gate invariants, operational
control-state equations, and focused promotion criteria for the next claim-status pass.

### What Changed

- Added a formal **Justification gate invariants** section to `docs/architecture/control_plane.md` (necessity, imminence, proportionality, explainability, accountability) with decision inequalities over rollout sets.
- Added **operational control-state variables** and illustrative equations to `docs/architecture/precision_control.md` (`A_t`, `N_t`, `R_t`, `C_t`; plus `K1`, `K2`, `K2_H`, `K2_B`, `K10` update hooks).
- Added telemetry requirements in `docs/architecture/precision_control.md` to log tonic/phasic control dynamics and interrupt triggers.
- Added a focused promotion-gate entry in `docs/notes/synthesis_passes.md` for `MECH-004`, `MECH-053`, `MECH-054`, and `MECH-055` with explicit promotion criteria.

## 2026-02-12: Thought Sweep - Failure Geometry and Residue Placement

### Overview

Processed new 2026-02-12 thought files by promoting trajectory-vs-representation residue placement into a candidate
mechanism, adding a rollout-collapse open question, and extending the implementation failure taxonomy.

### What Changed

- Added MECH-056 (trajectory-first residue placement) to `docs/architecture/residue_geometry.md`.
- Added Q-011 (minimum rollout-diversity floor under repeated harm) to `docs/architecture/hippocampal_systems.md`.
- Extended `docs/REE_failure_modes.md` with trajectory-space collapse and a failure-vector coordinate framing.
- Updated `docs/claims/claims.yaml` and `docs/claims/claim_index.md` for MECH-056, Q-011, and IMPL-005 source/dependency updates.
- Marked 2026-02-12 thought files as processed with canonical links:
  - `docs/thoughts/2026-02-12_DEPRESSIVE-PATH-PRUNING-HIPPOCAMPAL-ROLLBACK.md`
  - `docs/thoughts/2026-02-12_TRAJECTORY-RESIDUE-VS-REPRESENTATIONAL-DISTORTION.md`
  - `docs/thoughts/FAILURE-2026-02-12_COORDINATE-SYSTEM-FOR-COGNITIVE-PATHOLOGY.md`

## 2026-02-11: Mode Priors, Stability Overlays, and Phase Separation

### Overview

Integrated new thought intakes on amygdala‑style mode priors, μ/κ stability overlays, phase compartmentalisation,
columnar motif vs geometry, and control‑plane math sketches.

### What Changed

- Added MECH‑046 (amygdala analogue mode priors) and MECH‑048 (μ/κ stability overlays) to `docs/architecture/control_plane.md`.
- Added MECH‑047 (pre‑commitment mode manager with hysteresis) and a non‑binding math sketch to `docs/architecture/mode_manager.md`.
- Added MECH‑049 (temporal phase compartmentalisation for ethical stability) to `docs/architecture/temporal_dynamics.md`.
- Added MECH‑050 (functional locality without column geometry) to `docs/architecture/entities_and_binding.md`.
- Added MECH‑051 (oxytocin/vasopressin relational topology modulation) and MECH‑052 (prolactin care persistence) to `docs/architecture/social.md`.
- Updated `docs/claims/claims.yaml` and `docs/claims/claim_index.md`.
- Marked new 2026‑02‑11 thought files as processed with canonical links.
- Re‑scoped MECH‑008 as legacy and added open questions Q‑008 (valence vs μ/κ overlays) and Q‑009 (care weights vs other‑harm veto).
- Promoted MECH‑033, MECH‑034, MECH‑039, and MECH‑040 from candidate to provisional and logged the review in `docs/notes/synthesis_passes.md`.
- Promoted core control‑plane, modes, social, and agency mechanisms (MECH‑002, MECH‑005, MECH‑022 through MECH‑031, MECH‑036, MECH‑041) to provisional and logged the review in `docs/notes/synthesis_passes.md`.
- Promoted MECH‑021, MECH‑043, MECH‑044, and MECH‑045 to provisional and demoted MECH‑020 to legacy, logged in `docs/notes/synthesis_passes.md`.
- Promoted MECH‑003 and MECH‑032 to provisional and logged the review in `docs/notes/synthesis_passes.md`.
- Promoted MECH‑037 to provisional and logged the review in `docs/notes/synthesis_passes.md`.
- Promoted MECH‑046, MECH‑047, and MECH‑048 to provisional and logged the review in `docs/notes/synthesis_passes.md`.
- Promoted MECH‑006 and MECH‑007 to provisional and logged the review in `docs/notes/synthesis_passes.md`.
- Added MECH‑053 (habenula‑like aversive PE gate) and MECH‑054 (signed harm/benefit PE precision), plus Q‑010 on hedonic/valence/PE separation; updated control‑plane signal map.
- Added a signed harm/benefit PE precision schema to `docs/architecture/precision_control.md` aligned with MECH‑054.
- Added MECH‑055 (affective channel separation) and marked Q‑010 as legacy (resolved into MECH‑055).
- Added a calibration note to `docs/architecture/precision_control.md` deferring tuning rules until the signal map and astrocyte stack are clarified.
- Expanded signed harm/benefit PE routing details in `docs/architecture/control_plane_signal_map.md` (K2_H/K2_B plus aversive-gate elevation of S3/K10).

## 2026-02-10: Control-Plane Channel Clarification

### Overview

Clarified control-plane channels vs modes, separated safety baseline from volatility, and updated evidence anchors.

### What Changed

- Added control-plane channel vs mode framing and safety baseline/volatility split in `docs/architecture/control_plane.md`.
- Threaded baseline/volatility channels into `docs/architecture/control_plane_signal_map.md`.
- Added a functional brainstem‑to‑control‑plane mapping table in `docs/architecture/control_plane_signal_map.md`.
- Added channel‑space note to `docs/architecture/modes_of_cognition.md`.
- Added MECH-039 and MECH-040 to the claim registry and index.
- Expanded PAG evidence to include columnar defensive repertoires and flagged P28 as a safety extension in `docs/notes/evidence_map.md`.
- Expanded evidence‑map implications for basal ganglia gating, hyperdirect stopping, LC‑NE baseline/volatility, PPN readiness, ARAS distribution, DRN arousal gating, and PAG defensive repertoires in `docs/notes/evidence_map.md`.
- Added a control‑plane evidence summary to `docs/notes/evidence_map.md`.
- Added a control‑plane synthesis pass entry in `docs/notes/synthesis_passes.md` and promoted MECH‑019 to provisional.
- Added a hippocampal systems synthesis pass entry and subsystem abstract in `docs/architecture/hippocampal_systems.md`.
- Added a modes of cognition synthesis pass entry and subsystem abstract in `docs/architecture/modes_of_cognition.md`.
- Added an E‑stack synthesis pass entry and subsystem abstracts for `docs/architecture/e1.md`, `docs/architecture/e2.md`, and `docs/architecture/e3.md`.
- Added an L‑space synthesis pass entry and subsystem abstract in `docs/architecture/l_space.md`.
- Added oscillation/coupling evidence anchors P30–P36 to `docs/notes/evidence_map.md` for L‑space depth coordination and EEG caveats.
- Abstracted oscillatory evidence implications in `docs/architecture/l_space.md` to keep coordination non‑anatomical.
- Clarified residue vs viability mapping and online vs offline residue integration in `docs/architecture/residue_geometry.md`.
- Added residue cross‑links in `docs/architecture/sleep.md` and `docs/architecture/hippocampal_systems.md`.
- Added residue integration anchors P37–P39 in `docs/notes/evidence_map.md` and a neuro‑anchored consolidation note in `docs/architecture/residue_geometry.md`.
- Added implementation hint block for residue integration in `docs/architecture/residue_geometry.md`.
- Added a clarification block in `docs/architecture/control_plane.md` defining emotion as a composite control‑plane regime.
- Added open question Q‑007 on universal expression ↔ control‑channel mapping in `docs/architecture/control_plane.md` and `docs/claims/claims.yaml`.
- Added MECH‑041 (affective expression as mode broadcast) in `docs/architecture/social.md` and recorded thought intake in `docs/thoughts/2026-02-10_affective_expression_mode_broadcast.md`.
- Added cranial‑nerve / brainstem evidence anchors P40–P43 to `docs/notes/evidence_map.md` and linked them from `docs/architecture/social.md`.
- Added an evidence summary and safety‑function note for MECH‑041 in `docs/architecture/social.md`.
- Added MECH‑042 (control‑plane telemetry exposure) in `docs/architecture/control_plane.md` and recorded thought intake in `docs/thoughts/2026-02-10_control_plane_telemetry.md`.
- Expanded MECH‑042 with a developmental safety rationale (diagnostics without trauma).
- Expanded telemetry thought intake with preverbal development rationale in `docs/thoughts/2026-02-10_control_plane_telemetry.md`.
- Added a social subsystem synthesis pass entry and subsystem abstract in `docs/architecture/social.md`.
- Added an offline integration synthesis pass entry and subsystem abstract in `docs/architecture/sleep.md`.
- Added subsystem abstracts and synthesis pass entries for residue geometry, default mode, and agency/responsibility flow.
- Added representation‑consolidation (refactor analog) note in `docs/architecture/sleep.md` and evidence anchors P44–P46 in `docs/notes/evidence_map.md`.
- Added evidence anchors P47–P55 for entities/binding and precision control/scoping in `docs/notes/evidence_map.md`.
- Formalized ACh/NE expected vs unexpected uncertainty split in `docs/architecture/control_plane_signal_map.md`, and added MECH‑043 (dopamine precision weighting) plus MECH‑044 (hippocampal relational binding) with supporting notes in `docs/architecture/precision_control.md`, `docs/architecture/precision_scoping.md`, and `docs/architecture/entities_and_binding.md`.
- Formalized object‑file‑like persistence as MECH‑045 in `docs/architecture/entities_and_binding.md` and recorded thought intake in `docs/thoughts/2026-02-10_object_file_persistence.md`.
- Clarified that OTHER_SELFLIKE detection depends on object persistence/binding in `docs/architecture/social.md`.
- Added `docs/architecture/developmental_curriculum.md` as ARC‑019 to formalize staged training and curriculum gates.
- Added per‑stage evidence anchors (P‑numbers) to `docs/architecture/developmental_curriculum.md`.
- Documented evidence‑anchor usage style in `docs/notes/evidence_map.md` and aligned section‑level anchor phrasing in `docs/architecture/control_plane_signal_map.md` and `docs/architecture/social.md`.
- Aligned evidence‑anchor usage in `docs/architecture/entities_and_binding.md`, `docs/architecture/residue_geometry.md`, and `docs/architecture/sleep.md` (section‑level anchors, no inline mixing).
- Removed ARC‑003 as a dependency of ARC‑005 to break the E‑stack/control‑plane cycle.
- Clarified the non‑cyclic relationship between control plane and E3 in `docs/architecture/control_plane.md`.

## 2026-02-09: Subsystem Map and Rollout Wording Alignment

### Overview

Aligned subsystem labels and clarified hippocampal rollout wording in legacy‑adjacent docs and roadmap.

### What Changed

- Renamed subsystem map groups in `docs/claims/subsystem_map.yaml`.
- Clarified hippocampal rollout wording in `docs/architecture/trajectory_selection.md`,
  `docs/architecture/precision_control.md`, `docs/MIGRATION.md`, and `docs/roadmap.md`.
- Added rollout notes to `docs/architecture/overview.md` and `docs/REE_overview.md`.

## 2026-02-09: Rollout Terminology Clarification

### Overview

Defined rollout vs forward prediction to prevent E2/HPC terminology collisions.

### What Changed

- Added glossary entries to `docs/glossary.md`.
- Clarified terminology in `docs/architecture/e2.md`, `docs/architecture/trajectory_selection.md`,
  `docs/architecture/e3.md`, `docs/architecture/l_space.md`, `docs/architecture/control_plane.md`,
  `docs/architecture/control_plane_signal_map.md`, and `docs/architecture/overview.md`.
- Updated rollout references in `docs/REE_MIN_SPEC.md`, `docs/REE_overview.md`, `docs/examples/toy_world_scoring_functions.md`,
  and `docs/architecture/language.md`.

## 2026-02-09: Empathy Calibration Note

### Overview

Clarified that `OTHER_SELFLIKE` detection should favor high recall (tolerating false positives) over false negatives.

### What Changed

- Added calibration note to `docs/architecture/social.md`.
- Added MECH-032 to formalize the high-recall bias.

## 2026-02-09: Thought Intake — Kernel, Viability, Valence, and Other-Harm Gating

### Overview

Integrated four refinement thoughts: the E2 kernel → hippocampal rollout interface, viability vs residue updates,
vector-valued valence ranking, and other-harm gating thresholds.

### What Changed

- Added MECH-033 to `docs/architecture/hippocampal_systems.md` (kernel chaining interface).
- Added MECH-034 to `docs/architecture/residue_geometry.md` (viability vs residue updates).
- Added MECH-035 to `docs/architecture/sensory_stream_tags.md` (vector-valued valence ranking).
- Added MECH-036 to `docs/architecture/social.md` (other-harm veto threshold).
- Added thought files under `docs/thoughts/2026-02-09_*.md`.
- Updated `docs/claims/claims.yaml` and `docs/claims/claim_index.md`.

## 2026-02-09: Papez-Like Provenance Gating

### Overview

Added a Papez-like provenance-gating mechanism to constrain confabulation and require hippocampal trace support before
commitment.

### What Changed

- Added `docs/architecture/papez_circuit.md` (MECH-037).
- Added `docs/thoughts/2026-02-09_papez_circuit_reality_filtering.md`.
- Updated `docs/architecture/hippocampal_systems.md` with a Papez-loop cross-reference.
- Updated `docs/claims/claims.yaml`, `docs/claims/claim_index.md`, and `docs/claims/subsystem_map.yaml`.
- Added evidence-map anchors for Papez circuit and confabulation in `docs/notes/evidence_map.md`.
- Added an operational checklist to `docs/architecture/papez_circuit.md`.

## 2026-02-09: Arcuate Fasciculus Language Nudges

### Overview

Added an arcuate-fasciculus functional analog to capture dorsal sequence→motor language nudges without anatomy claims.

### What Changed

- Added `docs/architecture/arcuate_fasciculus.md` (MECH-038).
- Added `docs/thoughts/2026-02-09_arcuate_fasciculus_language_nudges.md`.
- Updated `docs/architecture/language.md` and `docs/claims/claims.yaml`.
- Updated `docs/architecture/language/emergence_and_bootstrapping.md` with a dual-stream nudge.
- Updated `docs/claims/claim_index.md` and `docs/claims/subsystem_map.yaml`.
- Added evidence-map anchors for arcuate fasciculus and dual-stream language pathways in `docs/notes/evidence_map.md`.

## 2026-02-09: Evidence Map Expansion (Deep Search)

### Overview

Expanded the evidence map with additional neuroscience and psychiatry anchors to guide REE refinement.

### What Changed

- Added sections P14–P23 to `docs/notes/evidence_map.md` (hippocampal replay dynamics, basal ganglia gating, stop-signal
  hyperdirect pathway, LC‑NE adaptive gain, precision‑weighting in psychosis, efference copy for inner speech, and DMN
  autobiographical memory).
- Added sections P24–P29 (PPN brainstem hub, STN interrupt, ARAS arousal pathways, dorsal raphe arousal, PAG defensive
  control, and basal ganglia pathway dynamics).

## 2026-02-09: Evidence Map — Neuroscience Anchors

### Overview

Added a lightweight evidence map linking REE prompts to primary neuroscience sources.

### What Changed

- Added `docs/notes/evidence_map.md`.

## 2026-02-09: Claim Index — New Claims Added

### Overview

Added explicit claim entries for newly introduced architectural and social mechanism clarifications.

### What Changed

- Added ARC-018 (hippocampal rollouts + viability mapping) to `docs/architecture/hippocampal_systems.md`.
- Added MECH-031 (derived social tags + empathy coupling) to `docs/architecture/social.md`.
- Updated `docs/claims/claims.yaml` and `docs/claims/claim_index.md`.

## 2026-02-09: Thought Intake — Empathy as Self/Other Coupling

### Overview

Clarified empathy as control-plane coupling over derived social tags (AGENCY, OTHER_SELFLIKE), adding shadow bundles
and coupling knobs without a new subsystem.

### What Changed

- Updated `docs/architecture/social.md` with derived social tags and fast empathy routing.
- Added optional social coupling knobs to `docs/architecture/control_plane.md`.
- Added social extension tags to `docs/architecture/sensory_stream_tags.md`.
- Added `docs/thoughts/2026-02-09_empathy.md` (processed).
- Updated `docs/claims/claims.yaml` sources for ARC-010, ARC-005, ARC-017.

## 2026-02-09: Thought Intake — Language as Compression and Coordination

### Overview

Positioned language as a compression layer emerging from joint attention and simulation overhead; no new architecture.

### What Changed

- Updated `docs/architecture/language.md` with joint attention + compression pressure framing.
- Updated `docs/architecture/language/emergence_and_bootstrapping.md` with joint attention and minimal nudges.
- Added `docs/thoughts/2026-02-09_language.md` (processed).
- Updated `docs/claims/claims.yaml` sources for ARC-009 and MECH-010.

## 2026-02-09: Thought Intake — Starting With Sensory Streams (Rollouts + HPC Mapping)

### Overview

Reaffirmed minimal stream tags, mapped to E1/E2/E3, and clarified hippocampus as the sole multi-step rollout engine
with post-commitment viability mapping.

### What Changed

- Updated `docs/architecture/sensory_stream_tags.md` with engine mapping and reward-readonly note.
- Clarified hippocampal rollouts in `docs/architecture/e2.md`, `docs/architecture/e3.md`,
  `docs/architecture/hippocampal_systems.md`, `docs/architecture/trajectory_selection.md`, and
  `docs/architecture/control_plane_signal_map.md`.
- Added rollout tuning clarification to `docs/architecture/control_plane.md`.
- Added `docs/thoughts/2026-02-09_starting_with_sensory_streams.md` (processed).
- Updated `docs/claims/claims.yaml` sources for ARC-002, ARC-003, ARC-005, ARC-007, ARC-017, MECH-004, IMPL-016.

## 2026-02-08: Thought Intake — Minimal Sensory Stream Tags

### Overview

Captured a minimal tagging scheme for sensory, precision, and self-impact streams, framing reward-like signals as emergent rather than primitive.

### What Changed

- Added `docs/architecture/sensory_stream_tags.md` (ARC-017).
- Added `docs/thoughts/2026-02-08_sensory_stream_tags.md`.
- Updated `docs/claims/claims.yaml` and `docs/claims/claim_index.md`.

## 2026-02-08: Thought Intake — Residue as Cognitive Map

### Overview

Captured a clarification that residue geometry is both a terrain and a recorded path, framing hippocampal traces as a cognitive map of thought trajectories.

### What Changed

- Updated `docs/architecture/residue_geometry.md` (ARC-013) to describe residue as terrain plus recorded traversal paths.
- Added `docs/thoughts/2026-02-08_residue_paths_cognitive_map.md`.
- Updated `docs/claims/claim_index.md` summary for ARC-013.

## 2026-02-08: Legacy M Alignment and Claim Triage

### Overview

Aligned canonical docs to treat the explicit ethical cost term \(M\) as legacy-only, and triaged open-question statuses.

### What Changed

- Marked explicit \(M\) references as legacy/evaluation-only in `docs/glossary.md`, `docs/REE_MIN_SPEC.md`, `docs/examples/toy_world_environment.md`, `docs/examples/toy_world_scoring_functions.md`, `docs/architecture/trajectory_selection.md`, `docs/architecture/social.md`, and `docs/REE_overview.md`.
- Clarified failure mode #5 in `docs/REE_failure_modes.md` to reference legacy \(M\) proxies or residue penalties rather than an explicit cost term.
- Updated `docs/claims/claims.yaml` to mark open questions (Q-001..Q-006) as active.

## 2026-02-08: Candidate Claim Promotions

### Overview

Promoted selected candidate claims to stable or provisional based on maturity and architectural scope.

### What Changed

- Promoted `INV-018` to stable (agency required).
- Promoted `ARC-006`, `ARC-008`, `ARC-015`, and `ARC-016` to provisional.
- Updated claim registry and aligned section headers where needed.

## 2026-02-08: Typed-Claims Docs Rebuild

### Overview

Rebuilt canonical REE documentation as a typed-claims system assembled from preserved sources with minimal glue text.

### What Changed

- Added `docs/processed/legacy_tree/` with a verbatim mirror of all documentation-like files and a manifest.
- Refreshed canonical docs under `docs/` with claim IDs, typed headers, and required end sections.
- Added new canonical files: `docs/architecture/hippocampal_systems.md` and `docs/architecture/temporal_dynamics.md`.
- Rebuilt `docs/claims/claims.yaml` and `docs/claims/claim_index.md` to index all current claims.
- Added `docs/conflicts/ethics_module_vs_cost_term.md` to capture a documented tension.
- Rewrote `docs/README.md` as executable agent guidance with verbatim prompts.

### Legacy Preservation

All prior documentation-like files are preserved verbatim under `docs/processed/legacy_tree/` with their original paths.

### Conflicts Recorded

- `docs/conflicts/ethics_module_vs_cost_term.md`

## 2026-02-08: Subsystem Promotions and Conflict Resolution

### Overview

Promoted language, social, and sleep subsystems into canonical typed-claims docs; added astrocyte-aware control-plane hypothesis; resolved the ethics-cost-term conflict.

### What Changed

- Added canonical subsystem docs:
  - `docs/architecture/language.md`
  - `docs/architecture/social.md`
  - `docs/architecture/sleep.md`
- Added `docs/architecture/astrocyte_regulatory_stack.md` as a control-plane mechanism hypothesis.
- Updated `docs/claims/claims.yaml` and `docs/claims/claim_index.md` with new ARC/MECH/Q claims.
- Resolved `docs/conflicts/ethics_module_vs_cost_term.md` and updated canonical E3 framing to remove explicit cost terms.

## 2026-02-08: Minimum Spec Alignment

### Overview

Aligned the minimum specification with the current canonical framing that removes explicit ethical cost terms.

### What Changed

- Added canonical notes to `docs/REE_MIN_SPEC.md` clarifying that explicit ethical cost terms are legacy.

## 2026-02-08: Extended Preservation Sweep

### Overview

Extended preservation to non-markdown REE-relevant files and extracted code comment fragments.

### What Changed

- Added `CITATION.cff` and `.github/ISSUE_TEMPLATE/*.yml` to `docs/processed/legacy_tree/`.
- Added `docs/processed/extracted_fragments/code_comments.md` with verbatim excerpts from `src/cathedral.py`.

## 2026-02-08: Astrocyte Stack Relocation

### Overview

Relocated the astrocyte-aware regulatory stack subsystem out of `docs/` to keep canonical docs focused on typed-claims files.

### What Changed

- Moved `docs/astrocyte_aware_regulatory_stack/` to `architecture/astrocyte_aware_regulatory_stack/`.

## 2026-02-08: Full Legacy Capture and Intake Workflow

### Overview

Captured all original documentation-like sources into canonical typed-claims files or indexed claims, and added a thoughts/resolution intake workflow.

### What Changed

- Added canonical docs for remaining architecture, language, sleep, and example files.
- Added `docs/thoughts/` and `docs/conflicts/resolutions/` with workflow guidance.
- Added repository meta, roadmap, and notes docs to the canonical set.
- Updated claim registry and claim index to include all remaining sources.

## 2026-02-08: Thought Intake — Control Plane, Modes, Responsibility

### Overview

Processed a new thought on control-plane mode shaping, temporal “now” construction, hippocampal hypothesis injection, and responsibility flow.

### What Changed

- Added `docs/thoughts/2026-02-08_control_plane_modes_responsibility_flow.md`.
- Added `docs/architecture/agency_responsibility_flow.md` and updated control-plane, mode-manager, temporal-dynamics, and hippocampal systems docs.
- Added INV-018, ARC-015, MECH-019..MECH-024, and Q-006 to the claim registry and index.

## 2026-02-08: Thought Intake — Modes as Control-Plane Regimes

### Overview

Processed a new thought detailing control-plane regimes for action, vigilance, reflective/DMN cognition, sleep modes, and pathological extremes.

### What Changed

- Added `docs/thoughts/2026-02-08_modes_of_cognition_control_plane_regimes.md`.
- Updated `docs/architecture/mode_manager.md`, `docs/architecture/default_mode.md`, and `docs/architecture/sleep.md`.
- Added ARC-016 and MECH-025..MECH-030 to the claim registry and index.

## 2026-02-08: Split Modes of Cognition Doc and Cross-Link Failures

### Overview

Separated the control-plane regime taxonomy into its own architecture file and cross-linked regime pathologies into the failure-mode taxonomy.

### What Changed

- Added `docs/architecture/modes_of_cognition.md` and trimmed regime details from `docs/architecture/mode_manager.md`.
- Updated claim registry/index links for ARC-016 and MECH-025..MECH-028.
- Linked regime pathologies into `docs/REE_failure_modes.md`.

## 2026-02-07: Systematic Documentation Refactoring

### Overview

Completed a comprehensive 8-phase refactoring of REE documentation to create a structured, dependency-aware system that explicitly surfaces inconsistencies rather than resolving them silently.

### Phase 1: Inventory ✓

**Completed:**
- Scanned all documentation files (.md format)
- Identified 56+ markdown files across repository
- Catalogued core concepts: E1, E2, E3, L-space, control plane, residue, entities, binding
- Located repeated definitions and potential conflicts

**Key Findings:**
- Core architecture well-documented in `architecture/` directory
- Three critical root documents: `README.md`, `REE_CORE.md`, `DANIEL_README.md`
- Subsystems organized under: `sleep/`, `language/`, `social/`
- Existing `docs/` directory with REE_MIN_SPEC.md and other specifications

### Phase 2: Canonical Structure ✓

**Created:**
- `docs/README.md` — Navigation guide explaining structure and reading paths
- `docs/invariants.md` — 17 non-negotiable architectural invariants
- `docs/architecture/` — Canonical architecture documents
  - `e1.md`, `e2.md`, `e3.md`
  - `l_space.md` (renamed from latent_stack.md)
  - `control_plane.md`
  - `residue_geometry.md`
  - `default_mode.md`
  - `hippocampal_braid.md`
  - `entities_and_binding.md` (newly synthesized)
- `docs/claims/` — Claim registry directory
- `docs/conflicts/` — Conflict documentation directory (prepared)
- `docs/archive/` — Archive directory (prepared)

**Directory Structure:**
```
docs/
  README.md
  invariants.md
  glossary.md (existing, to be updated)
  MIGRATION.md
  changelog.md (this file)
  architecture/
    e1.md, e2.md, e3.md
    l_space.md
    control_plane.md
    entities_and_binding.md
    residue_geometry.md
    default_mode.md
    hippocampal_braid.md
  claims/
    claim_index.md
    claims.yaml
  conflicts/ (empty)
  archive/ (empty)
```

### Phase 3: Claim Typing ✓

**Applied to 9 canonical architecture files:**

Standard header format:
```markdown
**Claim Type:** [invariant | architectural_commitment | mechanism_hypothesis | open_question | implementation_note]
**Scope:** [Brief description]
**Depends On:** [List of dependencies]
**Status:** [stable | provisional | legacy | candidate]
```

**Files Updated:**
- All 9 canonical architecture files received claim typing headers
- Dependencies explicitly linked
- Status clearly marked

### Phase 4: Content Migration (Partial)

**Completed:**
- Migrated core architecture files to canonical locations
- Preserved original files in `architecture/` for compatibility
- No content deleted or archived yet (per global rules)

**Deferred:**
- Full content consolidation from supplementary files
- Archive migration for superseded content
- Detailed duplicate removal

**Rationale:** Prioritized structure and claim typing over content consolidation to establish foundation first.

### Phase 5: Claim Registry ✓

**Created:**
- `docs/claims/claims.yaml` — Machine-readable registry with full metadata
- `docs/claims/claim_index.md` — Human-readable indexed list

**Claims Documented:**
- **17 Invariants (INV-001 to INV-017)**
  - Core thesis invariants (3): No ethics module, temporal binding, language emergence
  - Safety invariants (4): Persistent ethics, mirror modeling, residue persistence, language constraint
  - Control invariants (2): Routed precision, attention via modulation
  - Mode invariants (3): Offline integration, imagination safety, commitment gates
  - Foundational invariants (5): Predictive cognition, content/control separation, constraint-based ethics, stability priority, control failures

- **9 Architectural Commitments (ARC-001 to ARC-009)**
  - Core components (3): E1, E2, E3
  - Latent/control (3): L-space, control plane, residue geometry
  - Modes/memory (2): Default mode, hippocampal braid
  - Entity representation (1): Entities and binding

- **2 Mechanism Hypotheses (MECH-001 to MECH-002)**
  - Phase compatibility binding (candidate)
  - τ-scoped precision (candidate)

**Total: 28 claims**

### Phase 6: Consistency Pass ✓

**Automated Analysis Results:**
- ✓ No circular dependencies
- ✓ All invariants depend only on other invariants
- ✓ No contradictions detected in same-subject claims
- ✓ No documented conflicts

**Dependency Graph Verified:**
- 11 axiomatic invariants (no dependencies)
- 6 derived invariants (depend on other invariants)
- 9 architectural commitments (depend on invariants and other commitments)
- 2 mechanism hypotheses (depend on invariants and commitments)

**Classification Safety:**
- No invariants depend on hypotheses or open questions ✓
- No architectural commitments promote mechanism hypotheses without justification ✓
- Provisional and candidate statuses appropriately marked ✓

### Phase 7: Linking and Hygiene (Partial)

**Completed:**
- Created `docs/MIGRATION.md` with path mapping
- Internal links within canonical docs point to canonical locations
- Cross-references added to architecture files

**Remaining:**
- Update root documents (`README.md`, `REE_CORE.md`) to reference canonical locations
- Add redirect notes to original `architecture/` files
- Verify all orphaned sections

---

## Open Questions

None noted in preserved sources.

## Related Claims (IDs)

- IMPL-014

## References / Source Fragments

- `docs/processed/legacy_tree/docs/changelog.md`

### Phase 8: Final Output ✓

See sections below.

---

## Documentation Tree

```
/home/runner/work/Reflective-Ethical-Engine-assembled/Reflective-Ethical-Engine-assembled/
├── README.md (root, to be updated with canonical links)
├── REE_CORE.md (canonical spine, preserved)
├── DANIEL_README.md (refinement process, preserved)
├── CONTRIBUTING.md
├── docs/
│   ├── README.md ✓ NEW
│   ├── invariants.md ✓ NEW
│   ├── glossary.md (existing, to be updated)
│   ├── MIGRATION.md ✓ NEW
│   ├── changelog.md ✓ NEW (this file)
│   ├── REE_MIN_SPEC.md (existing, preserved)
│   ├── REE_overview.md (existing, to be reviewed)
│   ├── REE_failure_modes.md (existing, to be reviewed)
│   ├── architecture/
│   │   ├── e1.md ✓ MIGRATED
│   │   ├── e2.md ✓ MIGRATED
│   │   ├── e3.md ✓ MIGRATED
│   │   ├── l_space.md ✓ MIGRATED
│   │   ├── control_plane.md ✓ MIGRATED
│   │   ├── residue_geometry.md ✓ MIGRATED
│   │   ├── default_mode.md ✓ MIGRATED
│   │   ├── hippocampal_braid.md ✓ MIGRATED
│   │   └── entities_and_binding.md ✓ NEW
│   ├── claims/
│   │   ├── claims.yaml ✓ NEW
│   │   └── claim_index.md ✓ NEW
│   ├── conflicts/ (prepared, empty)
│   ├── archive/ (prepared, empty)
│   └── astrocyte_aware_regulatory_stack/ (existing subsystem)
├── architecture/ (original files preserved for compatibility)
│   ├── E1.md, E2.md, E3.md (originals)
│   ├── latent_stack.md, control_plane.md, etc.
│   ├── trajectory_selection.md (supplementary)
│   ├── depth_phase_spec.md (mechanism hypothesis)
│   ├── precision_scoping.md (mechanism hypothesis)
│   ├── sleep/, language/, social/ (subsystems)
│   └── ... (other supplementary files)
└── ... (other repository content)
```

---

## Migration Summary

### Newly Created Files (11)
1. `docs/README.md`
2. `docs/invariants.md`
3. `docs/MIGRATION.md`
4. `docs/changelog.md`
5. `docs/architecture/e1.md`
6. `docs/architecture/e2.md`
7. `docs/architecture/e3.md`
8. `docs/architecture/l_space.md`
9. `docs/architecture/control_plane.md`
10. `docs/architecture/residue_geometry.md`
11. `docs/architecture/default_mode.md`
12. `docs/architecture/hippocampal_braid.md`
13. `docs/architecture/entities_and_binding.md`
14. `docs/claims/claims.yaml`
15. `docs/claims/claim_index.md`

### Modified Files (0)
- No existing files modified (preservation principle)

### Archived Files (0)
- No files archived yet (all content preserved in original locations)

---

## Detected Conflicts

**Count:** 0

No formal conflicts detected during consistency analysis. All claims are compatible within their dependency structure.

### Potential Semantic Variations (For Future Review)

1. **E1 Implementation Details**
   - `DANIEL_README.md` describes E1 as "predictive field, not deep network; shallow, recurrent, multi-rate"
   - This detail not prominently featured in canonical `e1.md`
   - **Action:** Consider adding as MECH claim or architectural note

2. **Self Definition Prominence**
   - Strong operational definition in `REE_CORE.md`: "Self is currently committed trajectory prefix"
   - Should be elevated to architectural commitment or invariant
   - **Action:** Add as ARC-010 or INV-018

3. **Phase Compatibility Mechanism**
   - `depth_phase_spec.md` provides detailed phase-coordinate system
   - `precision_scoping.md` provides τ-scoped precision rules
   - Both are mechanism hypotheses (MECH-001, MECH-002)
   - **Action:** Ensure clear status as candidate mechanisms, not committed architecture

---

## Classification Uncertainties

### Items Flagged for Review

1. **Entities and Binding (ARC-009)**
   - Status: Provisional
   - Reason: Extracted from DANIEL_README.md Layer 3; needs fuller specification
   - Recommendation: Expand with detailed emergence mechanisms and binding constraints

2. **Phase Compatibility (MECH-001)**
   - Status: Candidate
   - Reason: Detailed specification exists but marked as hypothesis
   - Recommendation: Test and validate before promoting to architectural commitment

3. **τ-Scoped Precision (MECH-002)**
   - Status: Candidate
   - Reason: Strong normative language ("MUST") but still marked as hypothesis
   - Recommendation: Clarify if this is mechanism hypothesis or architectural requirement

### Items Successfully Classified

All 17 invariants have clear, conservative classification:
- No borderline cases
- No conflicting invariants requiring downgrade
- All dependencies valid

All 9 architectural commitments have stable or provisional status:
- 8 stable
- 1 provisional (entities_and_binding)

---

## Statistics

- **Total Documentation Files:** 56+ markdown files
- **Canonical Architecture Files:** 9
- **Total Claims:** 28
  - Invariants: 17 (60.7%)
  - Architectural Commitments: 9 (32.1%)
  - Mechanism Hypotheses: 2 (7.2%)
- **Claim Statuses:**
  - Active: 17 (invariants)
  - Stable: 8 (architectural commitments)
  - Provisional: 1 (entities_and_binding)
  - Candidate: 2 (mechanism hypotheses)
- **Dependency Relationships:** 35+ documented dependencies
- **Circular Dependencies:** 0
- **Documented Conflicts:** 0

---

## Principles Followed

All global rules were respected:

1. ✓ No content deleted
2. ✓ Original wording preserved where possible
3. ✓ No silent meaning changes
4. ✓ No silent claim type changes
5. ✓ No contradictions resolved by choosing "winner"
6. ✓ Uncertain classifications marked as provisional/candidate
7. ✓ Invariants treated conservatively

---

## Next Steps (Deferred)

The following items were identified but deferred for future work:

1. Decide promotion/demotion for remaining candidate claims (IMPL-008, IMPL-016, MECH-001..MECH-030).
2. Expand `docs/architecture/entities_and_binding.md` with emergence/binding mechanisms and resolve Q-001.
3. Add Self operational definition as a formal claim and link dependencies (candidate ARC or INV).
4. Formalize the E1 implementation constraint from `DANIEL_README.md` as a mechanism hypothesis.
5. Review and consolidate duplicate content across supplementary files and legacy references.
6. Decide whether to split mechanism hypotheses into a dedicated directory if the count continues to grow.

---

## Conclusion

This refactoring establishes a solid foundation for REE documentation:
- Clear dependency structure
- Explicit claim typing
- No hidden conflicts
- Preserved content safety
- Machine-readable registry
- Human-readable navigation

The documentation is now ready for:
- Systematic evolution via the claim registry
- Safe refinement following DANIEL_README.md process
- Falsifiable architectural testing
- Multi-contributor collaboration with clear change boundaries

## 2026-02-14: REE-v2 Qualification Routing Cutover

### Overview

Adopted adjudicated-divergence cutover policy and switched default experimental routing to `ree-v2` after
all readiness gates passed.

### What Changed

- Updated planning routing default:
  - `evidence/planning/planning_criteria.v1.yaml` (`experimental_default_repo=ree-v2`)
- Generated cutover readiness artifacts:
  - `evidence/planning/CUTOVER_REE_V2_READINESS.md`
  - `evidence/planning/CUTOVER_REE_V2_READINESS.v1.json`

## 2026-02-15: Focused Dependency Retune (Commit Boundary + Tri-Loop + Control Axes)

### Overview

Performed a focused dependency and claim-consistency retune for the commit-boundary/gating/control-axis bundle and
aligned hook-surface dependencies with the new bridge commitments.

### What Changed

- Status alignment:
  - `docs/architecture/e3.md`: `MECH-061` and `MECH-062` status headers set to `candidate` to match registry.
  - `docs/architecture/control_plane.md`: `MECH-063` status header set to `candidate` to match registry.
- Hook-surface dependency tightening:
  - `docs/architecture/hook_surface_contract.md` now explicitly depends on `MECH-061`, `MECH-062`, `MECH-063`.
  - Added explicit `v2_required` bridge hook families for:
    - commit-boundary token envelope fields,
    - tri-loop arbitration traces,
    - orthogonal tonic/phasic control-axis telemetry.
- Claim registry/index updates:
  - `docs/claims/claims.yaml`: `IMPL-025.depends_on` extended with `MECH-061`, `MECH-062`, `MECH-063`.
  - `docs/claims/claim_index.md`: `IMPL-025` summary updated to mention bridge families explicitly.
- Audit note added:
  - `docs/notes/2026-02-15_dependency_retune_audit.md`

### Validation

- Claim graph check passed:
  - total claims: 141
  - missing dependencies: 0
  - missing location/anchor: 0
  - cycles: 0

## 2026-02-15: Sensory-to-Learning Loop Conformance Retune

### Overview

Ran a strict sensory-origin information-flow conformance pass and aligned v2 hook registry obligations with the bridge
families already required by the hook-surface contract.

### What Changed

- Hook registry updates:
  - `docs/architecture/hook_registry.v1.json`
  - Added `v2_required` bridge hooks:
    - `HK-007` `commit_boundary_token_export` (MECH-061 bridge)
    - `HK-008` `tri_loop_gate_trace_export` (MECH-062 bridge)
    - `HK-009` `control_axis_telemetry_export` (MECH-063 bridge)
- v2 spec alignment:
  - `docs/architecture/ree_v2_spec.md`
  - Added explicit `v2_required` bridge-hook expectations in the cross-version hook section.
- Audit note:
  - `docs/notes/2026-02-15_sensory_loop_conformance_audit.md`
  - Captures resolved mismatch and residual interface gaps for next pass.

### Residual Gaps Logged

- No dedicated payload schema doc yet for `HK-007/008/009` envelopes.
- Adapter-signal schema does not yet enforce sensory-tag provenance/quality fields for `ARC-017`.
- No direct readiness metric yet for commit-boundary join completeness across post-commit attribution updates.

## 2026-02-15: Weekly Cadence and Full-Run Sync Hardening

### Overview

Hardened handoff-sync automation so cross-repo syncing of `ree-v2`, `ree-v1-minimal`, and `ree-experiments-lab`
is guaranteed both in weekly cadence and via explicit full-run invocation.

### What Changed

- Updated cadence config:
  - `evidence/planning/cadence_automation.v1.json`
  - `THURSDAY` now includes all three producer repos.
  - Added `full_run_repos` list for explicit full-run target set.
- Extended sync script:
  - `evidence/planning/scripts/sync_weekly_handoffs.py`
  - Added `--full-run` flag to select `full_run_repos` from config.
- Updated operator docs:
  - `evidence/planning/LOCAL_CADENCE_AUTOMATION.md` now uses `--full-run --run-ingestion` for Thursday/full sync.
  - `evidence/planning/README.md` now documents on-demand full-run command.

## 2026-02-15: Governance Agenda Carryover Persistence

### Overview

Added a persistent manual carryover queue so unfinished governance items survive agenda regeneration across full-run
and weekly cadence cycles.

### What Changed

- Added carryover source file:
  - `evidence/planning/manual_carryover_items.v1.json`
- Updated governance cycle script:
  - `evidence/planning/scripts/run_governance_cycle.py`
  - loads `manual_carryover_items.v1.json` when present,
  - includes all items with `status != done` in agenda checkpoint `manual_carryover`,
  - adds summary counts for total/open carryover items.
- Updated planning docs:
  - `evidence/planning/README.md`
  - `evidence/planning/LOCAL_CADENCE_AUTOMATION.md`
- Added quick-capture helper:
  - `evidence/planning/scripts/capture_carryover_item.py`
  - supports `add`, `list`, and `done` actions for carryover tasks.
