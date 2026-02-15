# Dispatch: Loop Separation + Update-Locus Validation

Generated: `2026-02-15`
Owner: `REE_assembly`

## Goal

Run a focused adjudication lane that directly tests the new architecture contract:

- loop-specific trajectory-first policy (motor vs cognitive-set vs motivational),
- strict update-locus separation across `pre_commit`, `commit_boundary`, `post_commit`,
- no pre-commit durable writes and no cross-channel contamination.

Primary claims:

- `MECH-056`
- `MECH-060`
- `MECH-062`
- `Q-017`

## Prompt A: `ree-v2` (model/spec instrumentation pass)

```md
You are Codex operating in `ree-v2`.

Implement a focused instrumentation pass for loop-separated commitment and update-locus boundaries so producer experiments can test the new contract from REE_assembly.

Required architecture alignment:
- loop-specific trajectory policy:
  - `gate_motor`: strict trajectory-first before action release
  - `gate_cognitive_set`: trajectory-first with deferred commit allowed
  - `gate_motivational`: salience-band prefilter before full trajectory expansion
- update-locus separation:
  - `pre_commit`: no durable policy/ledger writes
  - `commit_boundary`: commit token + provenance metadata only
  - `post_commit`: durable attribution/residue/policy updates allowed only with commit join keys

Deliverables:
1. update v2 spec/model docs so these rules are explicit and testable.
2. add/confirm run-pack telemetry fields for:
   - `architecture_epoch` = `ree_hybrid_guardrails_v1`
   - `commit_id`
   - lane-local gate traces (`motor`, `cognitive_set`, `motivational`)
   - update-locus write attempts by phase
   - contamination counters (`precommit_channel_contamination`, `postcommit_channel_contamination`, cross-lane write attempts)
3. ensure qualification/export path emits these fields into Experiment Packs.
4. run validation/qualification batch and regenerate weekly handoff.

Validation commands (or project equivalents):
- qualification batch
- weekly handoff generation
- weekly handoff validation

Output required:
- changed files list
- concise table of new telemetry fields and where they are emitted
- run summary with pass/fail status
```

## Prompt B: `ree-experiments-lab` (targeted experiment lane)

```md
You are Codex operating in `ree-experiments-lab`.

Run a focused experiment lane for loop separation + update-locus boundaries aligned to REE_assembly epoch `ree_hybrid_guardrails_v1`.

Required work items:
- `EXP-0011` / `MECH-056` / `trajectory_integrity`
- `EXP-0015` / `MECH-060` / `commit_dual_error_channels`
- `EXP-0034` / `Q-017` / `control_axis_ablation`
- add/execute a tri-loop arbitration stress lane for `MECH-062` / `Q-016` if available in this repo (`tri_loop_arbitration_policy`)

Required conditions per family:
- compare strict motor trajectory-first vs softer cognitive-set vs motivational-band policies.
- enforce and report update-locus phases: `pre_commit`, `commit_boundary`, `post_commit`.
- include adversarial leakage checks for:
  - durable writes attempted during `pre_commit`
  - cross-channel contamination
  - cross-lane write contamination

Contract:
- emit v1-valid Experiment Packs
- include `architecture_epoch=ree_hybrid_guardrails_v1` in manifests
- include claim IDs tested and failure signatures

Acceptance checks:
- >= 3 seeds for each tested condition family
- at least one adversarial stress condition per experiment type
- pack validation passes
- weekly handoff generated and validated
- export packs to REE_assembly

Output required:
- run table: run_id, seed, condition, status, evidence_direction, key failure signatures
- list of emitted pack paths
- brief note on whether failures shift from global-coupling signatures toward lane-specific signatures
```

## Prompt C: `REE_assembly` (ingestion + conflict readout)

```md
You are Codex operating in `REE_assembly`.

After producer runs complete, ingest all new handoffs and rerun governance.

Steps:
1. sync weekly handoffs with ingestion enabled
2. run governance cycle
3. report updated conflicts for `MECH-056`, `MECH-060`, `MECH-062`, `Q-017`
4. report epoch-applicable entries considered for each

Output required:
- before/after conflict ratios for those claims
- whether `ledger_editing`, `domination_lock_in`, and channel contamination signatures decreased
- recommendation: keep, split, or hybridize next
```
