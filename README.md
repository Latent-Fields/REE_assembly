# REE Typed-Claims Documentation

`REE_assembly` is the canonical governance and specification repository for the Reflective Ethical Engine (REE).
It is documentation-first and decision-first: architecture, claims, evidence, and promotion decisions live here.
Implementation code and stress testing run in companion repositories, then feed evidence back here.

**Start here:** `docs/README.md`

## If You Are New (Read In This Order)

1. `docs/README.md` - operating procedure and required update discipline.
2. `docs/glossary.md` - canonical term definitions, including JEPA-to-REE translations.
3. `docs/architecture/e3.md` and `docs/architecture/control_plane.md` - commitment and control semantics.
4. `docs/roadmap.md` - current phase plan and repository roles.
5. `evidence/planning/REE_CONVERGENCE_INTERFACE.md` - how external knowledge enters REE.
6. `evidence/experiments/CROSS_REPO_SYNC_POLICY.md` - how implementation repos stay contract-aligned.

## What This Repository Owns

- Canonical REE architecture and claim registry (`docs/`, `docs/claims/`).
- Governance outcomes and promotion history (`evidence/decisions/`).
- Evidence intake boundaries and planning outputs (`evidence/experiments/`, `evidence/planning/`, `evidence/literature/`).
- Conflict capture without silent merge (`docs/conflicts/`).
- Historical source preservation (`docs/processed/legacy_tree/`).

## Architecture Snapshot (Plain Language)

- **E1**: slower, long-horizon predictive integration.
- **E2**: faster, short-horizon predictive transitions.
- **Hippocampal systems**: explicit multi-step rollout generation.
- **E3**: trajectory commitment engine. It is where responsibility becomes attributable.
- **Control plane**: regulation layer for precision, gain, mode, interruptibility, and commitment gating.

Commit semantics are continuous-stream, not stop-and-wait:

- Pre-commit and post-commit streams may both run continuously.
- The **commit boundary** is an authority boundary: irreversible dispatch and/or privilege-bearing durable-write eligibility for a `commit_id`.
- If interruption happens after irreversible dispatch, a **new superseding commit** is required; accountability lineage is extended, not erased.

## Ecosystem Map (How Repositories Work Together)

- `REE_assembly` (this repo): canonical claims, architecture, schemas, and governance decisions.
- `REE_convergence`: external-source intake, translation, provenance checking, and candidate deltas before promotion.
- `ree-v2`: qualification lane for substrate and contract stability.
- `ree-experiments-lab`: stress/adversarial and falsification lane.
- `ree-v1-minimal`: baseline/parity harness during transition and regression checks.
- `REE_OpenClaw`: external applied testbed consuming REE contracts and reporting handoff evidence.

## Knowledge Intake And Promotion Flow

This is the safe path for integrating implementation wisdom or external model insights:

1. Intake and translate in `REE_convergence` with explicit source provenance and license metadata.
2. Build a convergence promotion packet (candidate deltas only; no direct canonical overwrite).
3. Submit packet to `REE_assembly` inbox: `evidence/planning/convergence_packets/inbox/`.
4. Run queue validation and queue build:

```bash
python3 evidence/planning/scripts/validate_convergence_promotion_packet.py \
  --input-glob "evidence/planning/convergence_packets/inbox/*.json"
python3 evidence/planning/scripts/build_convergence_intake_queue.py
```

5. Human governance adjudicates accept/reject/hybridize/defer.
6. Only accepted deltas are promoted into canonical claims/docs/contracts, then dispatched to implementation repos.

## Cross-Repo Implementation Loop

Weekly cadence (current policy):

- Monday: `ree-v2` qualification handoff.
- Tuesday: `ree-experiments-lab` stress handoff.
- Wednesday: `ree-v1-minimal` parity/backstop handoff.
- Thursday: `REE_assembly` ingestion and governance cycle.
- Friday: decision packet and next dispatches.

## Core Guardrails

- Preserve history; do not silently overwrite prior formulations.
- Represent conflicts explicitly; do not hide unresolved tension.
- Do not copy unresolved external prose/code/weights directly into canonical architecture.
- Require provenance and license attribution before promotion.
- Keep schema contracts versioned and immutable once published.

## Working Structure

- `docs/` - canonical REE documentation and operating procedure.
- `docs/claims/` - claim registry (`claims.yaml`) and human index (`claim_index.md`).
- `docs/conflicts/` - documented conflicts and forks.
- `docs/thoughts/` - raw thought intake before canonical extraction.
- `docs/processed/legacy_tree/` - immutable preserved legacy sources.
- `evidence/experiments/` - experiment-pack ingestion boundary and contract artifacts.
- `evidence/literature/` - structured literature evidence linked to claims.
- `evidence/planning/` - backlog, interface packets, and dispatch planning.
- `evidence/decisions/` - persistent governance decision log.

## License And Citation

- License: Apache License 2.0 (`LICENSE`).
- Attribution and safety notice: `NOTICE`.
- Citation metadata (Daniel Golden): `CITATION.cff`.
