# Documentation Refactoring Changelog

**Claim Type:** implementation_note  
**Scope:** Documentation change history  
**Depends On:** None  
**Status:** stable  
**Claim ID:** IMPL-014
<a id="impl-014"></a>

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
