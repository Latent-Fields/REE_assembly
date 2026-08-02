# Failure Autopsy: V3-EXQ-108a (MECH-135 discriminative pair, StepHarness re-run)

**Generated:** 2026-08-02T10:50:16Z | **Status:** confirmed | **Scope:** single

## Facts

- Run: `v3_exq_108a_mech135_discriminative_pair_stepharness_20260802T035458Z_v3`, FAIL, claim MECH-135. Supersedes V3-EXQ-108.
- `multi_sense_audit_2026_05_08` found V3-EXQ-108's `_train_agent()` called `agent.sense()` TWICE per env step (once for `latent_prev`, once for `latent_next`), doubling the substrate-tick rate during training vs eval -- exactly the "double-sense pattern" `experiments/_harness.py`'s `StepHarness` class exists to make structurally impossible. 108a restructures `_train_agent` to call `sense()` exactly once per env step; Phases 1-6 (goal template, warmup, candidate generation, FROZEN/E1_COE scoring, real-env execution) are byte-identical to 108.
- Result: C1 (mean_prox_delta 0.00219 vs threshold 0.05) FAILS. C2 PASSES (1/1 seed needed). C3 (e1coe_score_var >= 0.002 per seed) FAILS: seed 42 var=1.494e-14, seed 123 var=9.47e-15 -- e1coe_score min/max/mean cluster within ~4e-7 of each other across 40 candidate sequences.
- **This nearly exactly replicates the original 108's real full-production FAIL** (2026-03-28, run `v3_exq_108_mech135_discriminative_pair_20260328T195341Z`: c1=0.00229, c3 var~1.4e-14) -- a run claims.yaml currently describes as "empty metrics -- runner artifact," which does not match the manifest (complete, non-empty). **Fixing the documented training confound did not change the outcome.**

## Why this matters beyond MECH-135

`_score_sequence_e1coe` computes `goal_state.goal_proximity(z_world_curr)` after rolling z_world forward through E1 for each of 40 candidate action sequences (`world_dim=32`). This is one of the most DIRECT possible tests of INV-088's coupling-leg prediction ("a low-effective-dimension z_world causes an evaluator built on it to assign near-identical value to distinct situations") -- no foraging policy, no AUC discretization, just distance-in-latent-space after 40 independently-imagined 30-step rollouts. The result is a near-machine-epsilon collapse (var ~1.5e-14), starker than either prior signal on this thread:

- V3-EXQ-744a: real-but-weak coupling (mean_delta_r2=0.130, rho=0.69 near-miss) -- WEAKENS but marginal.
- V3-EXQ-819/819a: sanctioned-trained z_world (`sd_zworld_warmup_optimizer_group`, confirmed 3/3 seeds trained) still only reaches AUC 0.90 vs a ~48-57 achievable ceiling -- "mild, non-load-bearing support" per claims.yaml's own 2026-07-26 note.
- **108a: near-total collapse, ~13 orders of magnitude below threshold**, via a mechanism (bare rollout-endpoint proximity) with essentially no intervening confound.

INV-088's own claims.yaml note records an open confound: every cell in the 2026-07-18 `zworld_near_static_characterisation` was **untrained** (0/61 latent_stack tensors moved during the x734 P0 warmup), so "(a1) encoder untrained" and "(a2) world_dim=32 discriminative-granularity ceiling" are "perfectly confounded in this data." **108a's z_world IS trained** (bespoke single-step MSE loss, 100 episodes) -- a genuinely new data point on the confound-breaking axis. But this bespoke loss is not the SANCTIONED training route 819/819a validated, so 108a cannot by itself rule out "(a1) this particular bespoke loss just isn't adequate" versus "(a2) genuine dimension ceiling."

## Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | weakened | E1_COE gives no measurable advantage; downstream of a scoring collapse |
| Biological reference | clear | co-evolving rollout mechanism implemented as designed |
| Prerequisites | present | Phases 1-6 unchanged, confound fix is a genuine improvement |
| Implementation | present, degenerate result | E1 rollout genuinely updates z_world; resulting scores don't discriminate |
| Measurement | adequate | direct, simple, unconfounded readout |
| Scale | **world_dim=32 -- likely proximate cause** | cross-references INV-088's open (a1)/(a2) confound |

## Fan-out recommendation (GOV-FANOUT-1)

Two live hypotheses, one experiment can address both:

- **H-undertrained-instrument (a1)**, axis=representation: re-run 108a's exact design but swap the bespoke-trained z_world for the sanctioned `sd_zworld_warmup_optimizer_group`-trained stack. Materially higher `e1coe_score_var` (clearing C3) supports (a1).
- **H-dimension-ceiling (a2)**, axis=measurement: on the same re-run, instrument the antecedent contrast-ratio metric (spread/||centroid||, per the 2026-07-18 characterisation methodology) directly on the 40 rollout endpoints. A low-and-untrainable contrast-ratio signature, even if `e1coe_score_var` improves somewhat, supports (a2).

Pre-registered in `hypothesis_space_registry.v1.json` as question `inv088_evaluator_degeneracy_cause`.

## Data-quality flag (separate from disposition)

claims.yaml's description of the original 108 full-production run as "empty metrics -- runner artifact" does not match the manifest (complete, non-empty, real thresholds). Flagged for governance to correct; not itself fixed here (claims.yaml is governance-only-edit territory).

## Routing

**epistemic_category:** `substrate_ceiling` | **evidence_direction:** `weakens` | **routing:** `/queue-experiment` -- the disambiguating experiment above, queued directly per explicit user instruction (2026-08-02) rather than deferred as a chip. `recommended bears_on: [INV-088]` for governance to add.

**User gate (2026-08-02):** User confirmed the INV-088 cross-reference is significant and directed that a disambiguating experiment be queued to resolve the confound conclusively, in this session.
