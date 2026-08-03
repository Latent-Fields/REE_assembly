# Failure Autopsy: V3-EXQ-108b (MECH-135/INV-088 z_world evaluator-degeneracy disambiguation)

**Generated:** 2026-08-03T08:42:37Z | **Status:** confirmed | **Scope:** single

## Facts

- Run: `v3_exq_108b_mech135_inv088_zworld_disambiguation_20260802T121643Z_v3`, FAIL, claims MECH-135/INV-088. Not a dry run (`check_dry_run_citations.py`: 1 clean). `non_degenerate: true`. Seeds 42/123.
- This run is the disambiguating experiment `failure_autopsy_V3-EXQ-108a_2026-08-02` fanned out for the `inv088_evaluator_degeneracy_cause` question, pre-registered with two live hypotheses:
  - **H-undertrained-instrument (a1)**: 108a's bespoke single-step E1 MSE loss was inadequate; the SANCTIONED `sd_zworld_warmup_optimizer_group` training route would clear C3.
  - **H-dimension-ceiling (a2)**: even sanctioned-trained, `world_dim=32` structurally cannot support enough discriminative capacity.
- 108b restructures Phase 0 into 0a (sanctioned SD-070 encoder warmup, the exact route V3-EXQ-819/819a validated) + 0b (108a's unchanged bespoke E1/E2 single-step training, now on top of the pre-trained encoder), then extends Phase 4 to capture each candidate's z_world ENDPOINT and adds Phase 4b (40 real, diverse z_world observations via independent random-policy rollouts).
- **Both readiness preconditions MET, both seeds:** `encoder_trained` (min `world_encoder_max_abs_delta` 0.224, guard-checked, holdout balanced accuracy 0.80-0.94 across hazard/resource-presence/distance probes) and `real_zworld_nondegenerate` (CR_real 0.193/0.201).
- **Load-bearing criterion C3_E1COE_SCORE_DISCRIMINATES FAILS both seeds**: `e1coe_score_var` 2.25e-14 (seed 123) / 1.65e-13 (seed 42, driven by a fp precision quirk in scores clustered at ~0.908) vs threshold 0.002 -- essentially machine-epsilon, matching 108a's original ~1.5e-14 almost exactly even with the sanctioned encoder swapped in.
- **New instrumentation resolves the driver's own decision tree, branch 3, exactly** (code-verified against `v3_exq_108b_mech135_inv088_zworld_disambiguation.py:846-853`): `CR_real` well above `CR_REAL_FLOOR=1e-4` (0.193-0.201) rules out branch 1 (dimension-ceiling); C3 fails so branch 2 (undertrained-instrument) does not fire; `CR_rollout/CR_real` = 2.57e-6 (seed 42) / 3.18e-6 (seed 123), both far below `CR_ROLLOUT_COLLAPSE_RATIO=0.1` -> branch 3, self-route `downstream_dynamics_collapse`. Self-route is trustworthy -- verified against the manifest's own raw numbers, not just the label.

## Root cause, traced in code (not inferred from the manifest alone)

`_train_agent` (unchanged from 108a) trains `agent.e1` via **single-step MSE only**: `agent.e1(total_prev, horizon=1)` against the very next real transition, 100 episodes. `_score_sequence_e1coe_with_endpoint` then applies that same `agent.e1` **autoregressively 30 times** (`rollout_horizon=30`), feeding each step's own prediction back in as the next input, to score each of 40 imagined candidate action sequences. This is the canonical model-based-RL failure mode: a dynamics model trained only on one-step transitions, rolled out far beyond its training horizon, has no objective preventing its own compounding error from converging toward a training-distribution-average attractor -- so 30 independently-imagined trajectories from 40 different action sequences end up landing on nearly the same predicted endpoint, regardless of which actions were fed in. This is orthogonal to whether the STATIC z_world representation (Phase 4b's real-state sample) can differentiate -- it clearly can (CR_real healthy) -- the collapse is specific to the autoregressive rollout dynamics.

## Claim-layer mapping

- **MECH-135**: stays `weakens` per 108a's DECLARED NULL (108b's own docstring: "A FAIL here (any label) does not reopen MECH-135's original C1/C2/C3 result -- 108a's weakens stands regardless of which explanation this run confirms"). 108b's own contribution to MECH-135 is `non_contributory` (explanatory, not an independent C1/C2/C3 retest).
- **INV-088** ("world_goal_evaluator_bounded_by_z_world_differentiation"): **user-confirmed reading: `weakens` (this pathway)**, not the manifest's own self-routed `non_contributory`. Rationale: INV-088's specific causal claim is that evaluator degeneracy is BOUNDED BY z_world's own differentiation-capacity. This run directly dissociates the two: z_world's real-state differentiation is healthy (CR_real 0.19-0.20) while the evaluator built on its rollout is still fully degenerate (C3 fails by ~11 orders of magnitude). In this pathway, evaluator failure is demonstrably NOT explained by z_world's differentiation-capacity -- it is explained by E1's rollout-dynamics training gap instead. That is direct evidence against the specific coupling INV-088 proposes, in this pathway.

## Biological-reference triage

Multi-step mental simulation / imagined-future construction depends, in mammals, on a hippocampal-neocortical scene-construction system distinct from (though built on top of) intact perceptual encoding -- constructive episodic simulation is understood to degrade with imagined temporal/step distance and to fail selectively (impoverished, less-detailed imagined scenarios) under damage to the simulation machinery even when perception of the present state is intact. That is the correct existence-proof shape for this finding: REE's z_world *encoder* (perception-analogue) is fine; its *rollout* mechanism (imagination-analogue) collapses distinctiveness over depth. This is presented as a plausible biological reference class for the follow-on lit-pull to verify with actual citations -- no specific paper is asserted here as REE literature, since none was found in `evidence/literature/` addressing this specific multi-step-rollout-consistency axis. The closest existing entry, `targeted_review_e2_forward_model_action_divergence` (2026-05-28), addresses a related but structurally distinct failure: E2's *single-step* per-action latent collapse (K actions predicting the same next-z_self), not E1's *multi-step autoregressive* collapse. Its ML literature (PLSM, contrastive RSSM, SWIRL) targets action-identifiability at one step, not long-horizon rollout consistency -- directly relevant as a design prior (all three are trainable-objective fixes to a latent dynamics model) but not a direct hit.

## Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | weakened (INV-088, this pathway) / non_contributory (MECH-135, per declared null) | dissociates evaluator failure from representation capacity |
| Biological reference | absent (for this specific axis) | plausible parallel (multi-step imagined-future construction vs intact perception) not yet lit-confirmed for REE; sibling E2 review covers a different axis |
| Prerequisites | present | SD-070 sanctioned encoder training confirmed engaged (guard-checked, holdout accuracy 0.80-0.94) |
| Implementation | complete, but training-objective mismatched to eval-time usage | E1 trained single-step, evaluated over a 30-step autoregressive rollout -- objective/usage mismatch, not a missing component |
| Environment | adequate | CausalGridWorldV2 with genuine hazard/resource structure; not implicated |
| Measurement | adequate | CR_real/CR_rollout instrumentation (this run's own new contribution) is exactly what was needed to disambiguate |
| Integration | isolated | E1's rollout is coupled to the goal-proximity evaluator but the collapse is intrinsic to E1 alone (real-state differentiation upstream is fine) |
| Scale | not implicated | world_dim=32 confirmed adequate for real-state differentiation (H-dimension-ceiling eliminated) |

## Hypothesis-space ledger (Step 9b)

Question `inv088_evaluator_degeneracy_cause` (registered 2026-08-02 by the 108a autopsy, `initial_frozen_count=2`):

- **H-undertrained-instrument**: resolved `eliminated` (full bar: `control_passed`+`non_degenerate`+`met_elimination_bar` all true). Basis: sanctioned-trained encoder confirmed engaged, C3 still fails.
- **H-dimension-ceiling**: resolved `eliminated` (full bar met). Basis: CR_real far above the degeneracy floor on the same sanctioned-trained encoder.
- **H-dynamics-collapse** (NEW): registered and resolved `confirmed` in the same edit, per Step 9b's same-cycle rule (`pre_registered_utc` set to the run's own completion date, preceding `resolved_utc` by construction since they're identical here). Axis `learning-signal` (constitution family, per the existing `axis_families.map`). Labelled as **fan-out growth** (invariant 3a): `fanout_growth_events` entry added citing this autopsy file as `fanout_source`, `initial_frozen_count_at_registration` preserved at 2, `initial_frozen_count` bumped to 3.
- `check_hypothesis_space_integrity.py` after the append: **0 flags (a/b/c/d)** for this question; the new leg's growth appears in the advisory labelled-fan-out-growth section, not as a violation.
- `decision.decidable` set to `true` -- the question now has an answer (a third mechanism, not either pre-registered one). `decision_log_ref` left null (human decision-log entry, not this skill's job).

## Re-derive brake (Step 7)

Recommended `epistemic_category`: **`competence_implementation_gap`** for both claims on this target -- explicitly NOT `substrate_ceiling`. This matters mechanically: MECH-135 currently carries 1 prior `substrate_ceiling` hit (108a); had 108b been stamped `substrate_ceiling` too it would reach the brake's default threshold (2) and force a refused-requeue onto `/implement-substrate`. That would be the WRONG read here -- 108b's entire point was to explain away the apparent ceiling, and it succeeded: the dimension-ceiling hypothesis is eliminated, not confirmed. Brake counts (re-checked via the standard R1-R3 recipe): MECH-135 stays at 1, INV-088 at 0. Brake does not fire for either claim.

## Learning extracted

1. INV-088's evaluator-degeneracy coupling, as literally framed (evaluator bounded by z_world's differentiation-capacity), is not the operative mechanism on this pathway -- a genuinely new, narrower, more specific mechanism (E1's single-step-trained forward model collapsing under long-horizon autoregressive rollout) is confirmed instead.
2. This disambiguation experiment is a clean example of a design that resolved its own pre-registered question by ELIMINATING both live hypotheses and surfacing a third -- the value of instrumenting the antecedent (CR_real) and the coupling-leg (CR_rollout) separately in the SAME run, rather than only the downstream scalar (e1coe_score_var).
3. A formal-ML training-objective import (single-step MSE for a component later used in multi-step rollout) with no dedicated biology/ML lit entry for this specific axis is exactly the case Step 4 flags: commission `/lit-pull` before committing to a specific fix, rather than assuming the sibling E2 review's conclusions transfer without checking.

## Routing

**Primary routing: `/lit-pull`** -- commission `targeted_review_e1_forward_model_rollout_consistency` (multi-step/long-horizon latent-dynamics training objectives, ML side: e.g. latent overshooting / scheduled multi-step unrolling / contrastive next-state prediction; biology side: multi-step imagined-future / mental-simulation degradation under intact-perception conditions). Explicitly note the sibling `targeted_review_e2_forward_model_action_divergence` as a strong methodological prior (same general problem class -- latent dynamics model objective choice) but not a substitute (different failure axis: single-step action-identifiability vs multi-step rollout-consistency).

**`recommended_substrate_queue_entry`** (action=`create`, pre-filled so `/implement-substrate` has a ready target once the lit-pull confirms a direction):

```json
{
  "action": "create",
  "sd_id_suggested": "SD-e1-rollout-consistency-training",
  "title": "E1 forward-model multi-step rollout-consistency training objective",
  "implementation_hint": "Add a multi-step/rollout-consistency term to E1's training objective (candidates per the /lit-pull commissioned above: latent overshooting, scheduled multi-step unrolling, or a contrastive next-state objective analogous to the E2 fix already surveyed) so autoregressive rollouts beyond the single-step training horizon do not collapse to a training-distribution-average attractor.",
  "unblocks_claims": ["INV-088", "MECH-135"],
  "depends_on_unresolved": ["targeted_review_e1_forward_model_rollout_consistency (lit-pull, not yet commissioned)"],
  "priority_suggested": 2,
  "failure_record_entry": {
    "run_id": "v3_exq_108b_mech135_inv088_zworld_disambiguation_20260802T121643Z_v3",
    "experiment_type": "v3_exq_108b_mech135_inv088_zworld_disambiguation",
    "metric": "e1coe_score_var (both seeds ~1e-13 to 1e-14) vs C3_VAR_THRESHOLD=0.002; CR_rollout/CR_real ratio ~3e-6 vs CR_ROLLOUT_COLLAPSE_RATIO=0.1",
    "target": "e1coe_score_var >= 0.002 and CR_rollout/CR_real >= 0.1 under a multi-step-trained E1"
  }
}
```

**Draft `evidence_quality_note`** (governance to write, INV-088):

> [failure_autopsy_V3-EXQ-108b_2026-08-03] V3-EXQ-108b (disambiguation of 108a's near-total evaluator-degeneracy) eliminates BOTH pre-registered hypotheses on `inv088_evaluator_degeneracy_cause`: the sanctioned-trained z_world encoder differentiates real states fine (CR_real 0.19-0.20, well above the degeneracy floor), ruling out both "bespoke loss undertrained" and "world_dim=32 is a structural ceiling." The actual bottleneck, confirmed in code and in both seeds: E1's forward-rollout model is trained only via single-step MSE (100 episodes) yet applied autoregressively 30 steps at eval time, collapsing 40 distinct imagined trajectories toward near-identical endpoints (CR_rollout/CR_real ~3e-6). Evidence direction: weakens (this pathway) -- the coupling INV-088 proposes (evaluator bounded by z_world differentiation) is dissociated from the observed failure, which is instead a training-objective/usage-horizon mismatch specific to E1. Routed to `/lit-pull` (targeted_review_e1_forward_model_rollout_consistency) before a substrate fix is committed.

**User gate (2026-08-03):** Confirmed via `AskUserQuestion` -- INV-088 scored `weakens` (this pathway) rather than the manifest's self-routed `non_contributory`; routing confirmed as `/lit-pull` first (not direct `/implement-substrate`).
