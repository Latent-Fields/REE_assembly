# Characterisation: the near-static character of `z_world`

**Date:** 2026-07-18
**Type:** DIAGNOSTIC measurement, offline. Not a queued experiment; governance-scoring-excluded.
**Licenses no build.** No `ree_core` change. No queue entry.
**Bears on:** INV-088 (z_world under-differentiation caps strategy diversity) — antecedent only.
**Does NOT bear on:** MECH-459 / the return-scale-normaliser thread, and NOT on either leg of the
live GOV-FANOUT-1 discrimination (V3-EXQ-780 H-bc-prior vs V3-EXQ-781 H-approach-primitive).
`mech457_competence_bootstrap_explorer` stays `blocked_pending_discrimination`.

---

## 1. Question

Convergence probe DREAMER-V3-P-008 (2026-07-18; write-up in
`REE_convergence/sources/dreamer-v3/actor_critic_stabilisation.md`, section "Probe
DREAMER-V3-P-008 -- result") recorded a limiting caveat: on CausalGridWorldV2 at the x734
`D3_hazard_free` rung, `z_world` is near-static — mean `||z_world||` 0.4623, mean one-step
movement 0.0094 (2.0% of norm), mean distance to centroid 0.0376, whole-dataset inter-state
spread 0.0522. The entire manifold spans ~0.05 around a centroid of norm 0.46, so `e2`'s 15-step
open-loop error (0.0698) exceeds the whole-dataset spread and a do-nothing persistence predictor
is an extremely strong baseline.

Three candidate causes, not discriminated at the time:

- **(a) ENCODER** — `z_world` under-differentiated by construction, independent of env and policy.
- **(b) RUNG** — `D3_hazard_free` is impoverished (no hazards, no reef, no proximity harm), so
  there genuinely is little state variation to encode.
- **(c) COMPETENCE** — trajectories are short-lived and low-competence (death at step 15-25), so
  the visited state distribution is a narrow early-episode slice.

## 2. Method

Offline harness, session scratchpad, uncommitted — the DREAMER-V3-P-008 pattern. Instantiates
`AgentV3` + `CausalGridWorldV2` via `x734._make_env` / `x724._make_agent(env, "all_on")`, senses
via `x742._sense`, and computes the statistics directly. Three passes:

1. **Manifold grid** — 4 rungs (`D0_baseline_724`, `D1_food_decoupled`,
   `D2_proximity_layout_derisked`, `D3_hazard_free`) x 2 seeds (42, 43) x 3 measurement policies
   (`random_walk`, `local_view_greedy`, `greedy_oracle` from `_lib/capability_eval.py`), 40 eval
   episodes x 200 steps per cell. 24 cells.
2. **Decodability** — held-out ridge readout of task-relevant variables, 2 rungs x 2 seeds.
3. **Weight-delta check** — does the x734 P0 warmup train the world encoder at all?

Two design choices carry the discrimination:

- **The encoder is held FIXED within a cell; only the measurement policy varies.** That isolates
  state-distribution effects (b)/(c) from the representation itself (a).
- **Every statistic is computed in parallel on two channels**: `z_world` (32-d latent) and
  `world_state` (the raw 250-d observation the encoder consumes). The raw channel is the control.
  If raw spread widens with rung richness or competence while `z_world` stays pinned, the
  variation EXISTS and the encoder is discarding it.

**Statistic choice.** Raw magnitude spread is not comparable across channels, because a biased MLP
adds a constant offset that inflates `||z||` without adding variance (`||centroid||` = 0.44 against
a spread of 0.042 — `z_world` is a large constant vector plus a small variation). The offset-invariant
statistic used here is the **contrast ratio, CR = spread / ||centroid||**: how distinguishable two
states are relative to the representation's own scale. Effective dimensionality is reported as the
participation ratio of the centred covariance spectrum (also offset-invariant).

## 3. Results

### 3a. The manifold grid — spread is invariant to BOTH rung and competence

Pooled by rung (mean over 2 seeds x 3 policies):

| rung | foraging | z_world CR | raw CR | z_world PR | raw PR |
|---|---|---|---|---|---|
| D0_baseline_724 (richest) | 4.15 | 0.0925 | 0.602 | 6.48 | 9.46 |
| D1_food_decoupled | 4.21 | 0.0901 | 0.579 | 6.70 | 9.56 |
| D2_proximity_layout_derisked | 35.34 | 0.0943 | 0.644 | 9.04 | 14.63 |
| D3_hazard_free (impoverished) | 36.20 | 0.1018 | 0.696 | 6.96 | 12.33 |

Pooled by measurement policy (mean over 4 rungs x 2 seeds):

| policy | foraging | survival | z_world CR | raw CR | z_world PR | raw PR |
|---|---|---|---|---|---|---|
| random_walk | 0.55 | 27.1 | 0.0929 | 0.636 | 6.83 | 8.59 |
| local_view_greedy | 27.80 | 93.7 | 0.0941 | 0.613 | 7.88 | 13.98 |
| greedy_oracle | 31.57 | 104.7 | 0.0969 | 0.642 | 7.18 | 11.92 |

Dynamic range across all 24 cells:

| quantity | range | fold |
|---|---|---|
| foraging | 0.075 -> 58.6 | **782x** |
| survival horizon | 11.3 -> 195.5 | **17.4x** |
| z_world contrast ratio | 0.0764 -> 0.1159 | **1.52x** |
| z_world pair-spread | 0.049 -> 0.067 | 1.4x |
| raw-observation PR | 5.59 -> 18.51 | 3.3x |
| z_world PR | 4.09 -> 9.74 | 2.4x |

**The `z_world` contrast ratio is ~0.094 everywhere.** It does not move across a 782-fold change
in foraging, a 17-fold change in survival horizon, or the full four-rung difficulty ladder. Note
the sign: the *impoverished* D3 rung has the **highest** contrast (0.1018) and the richest D0 rung
the lowest-but-one (0.0925) — rung impoverishment is not merely insufficient to explain the
tightness, it runs the wrong way.

The encoder attenuates contrast by a mean factor of **6.7x** (raw CR 0.63 -> z_world CR 0.094),
and that attenuation is itself constant across the grid (per-cell range 5.7x-7.9x).

Dimensionality partially transmits but is heavily attenuated. When the policy enriches the visited
set (`random_walk` -> `local_view_greedy`), raw PR rose in 8/8 cells (mean +5.4), while z_world PR
followed in only 6/8 (mean +1.05, ~5x attenuated) and *fell* in 2. Correlations across the grid:
`corr(foraging, raw_PR) = +0.73` but `corr(foraging, z_world_PR) = +0.39`.

### 3b. The mechanism: the world encoder is never trained

The `warm` (200-episode P0 warmup) cells came back **bit-identical to the untrained cells at four
decimal places** on every statistic and every policy. A direct weight-delta check confirms why:

```
after 20 episodes of x734._train_all_on_agent(p0_episodes=20, p1_episodes=0):
  latent_stack:  0/61 tensors changed
  e2:            6/18 tensors changed   (e.g. world_transition.0.weight max|d|=9.71e-01)
  world-path params in latent_stack: [split_encoder.world_precision_logit,
    split_encoder.world_encoder.{0,2}.{weight,bias}, split_encoder.world_topdown.{weight,bias},
    world_predictor.{weight,bias}]
  world-path CHANGED: NONE
```

The code path agrees: the P0 loop buffers `latent.z_world.detach()`
(`v3_exq_734_...py`, P0 inner loop) and optimises `Adam(agent.e2.parameters())` with
`clip_grad_norm_(agent.e2.parameters())` (`x724._e2_contrastive_step`,
`v3_exq_724_...py:433-463`). The gradient path terminates at a detached `z_world`, so
`latent_stack.split_encoder.world_encoder` receives no gradient.

**Under the x724/x734 configuration that DREAMER-V3-P-008 measured, `z_world` is a frozen,
randomly-initialised MLP projection of the observation** (`Linear(250,h) -> ReLU -> Linear(h,32)`,
`latent/stack.py:867-871`; no LayerNorm, so the tight spread is not a normalisation artefact). Its
geometry is fixed at initialisation. It *cannot* respond to rung richness or competence, which is
exactly what the grid measures.

### 3c. Decodability — the loss is task-relevant, and selectively so

Held-out ridge readout, `local_view_greedy` trajectories, 2 rungs x 2 seeds
(674 / 789 / 6559 / 7122 states). Raw observation is the achievable-information ceiling.

| target | z_world R^2 | raw R^2 | retained |
|---|---|---|---|
| agent_x | 0.715 | 0.880 | 81% |
| agent_y | 0.588 | 0.821 | 72% |
| resource_proximity | 0.461 | 0.817 | **56%** |
| nearest_resource_dist | 0.396 | 0.670 | **59%** |

The attenuation is not a harmless rescaling, but neither is it wholesale destruction. Spatial
self-location survives largely intact (72-81% retained); the **resource-relative** variables — the
ones a world/goal evaluator actually needs — lose 41-44% of decodable variance. The loss is
selective in the direction that matters for INV-088.

## 4. Verdict

**Cause (a) ENCODER, decisively, with a specific named mechanism** — and the mechanism is stronger
than "under-differentiated by construction": in this configuration the world encoder is *never
trained at all*. `z_world` is a frozen random projection whose contrast ratio (~0.094) is fixed at
initialisation and provably invariant to everything the environment or the policy can vary.

**Cause (b) RUNG: refuted.** Contrast is flat across the full four-rung ladder and is *highest* at
the most impoverished rung.

**Cause (c) COMPETENCE: refuted for manifold spread, but it OWNS the one-step-movement statistic.**
The two statistics dissociate, and the probe's headline "2.0% of norm" belongs to the second:

- Manifold spread / contrast ratio: invariant to competence (0.0929 -> 0.0969 across a 57-fold
  foraging change).
- One-step movement: strongly policy-dependent. 0.0094 for the probe's own REE policy, 0.028 for a
  random walk, 0.037 for `local_view_greedy` — i.e. the probe's low-competence agent moves through
  `z_world` **~3x more slowly than a random walk**, not merely slowly in absolute terms.

So the probe's two near-static observations have *different* causes. That the manifold spans only
~0.05 is an encoder fact. That the agent creeps across it at 2.0% of norm per step is a policy
fact — and a striking one in its own right, since a random walk beats it threefold.

**The probe's core conclusion for O6 is unaffected and is now better-grounded:** a lambda-return
over `e2` rollouts on this `z_world` would be degenerate, and the ceiling is upstream of `e2`. The
probe's caveat — that the measurement "cannot separate *e2 fails to model the dynamics* from
*`z_world` contains almost no dynamics to model*" — resolves toward the latter, with the added
finding that the encoder producing `z_world` was itself untrained during that measurement.

## 5. Bearing on INV-088 — antecedent supported, coupling untouched

INV-088 (`world_goal_evaluator_bounded_by_z_world_differentiation`) has two separable parts.

- **The antecedent** — that `z_world` differentiation is genuinely low — **gains direct
  quantitative support**: 6.7x contrast attenuation, 41-44% loss of decodable
  resource-relative variance, and a frozen-at-init encoder in the configuration measured. It also
  gains a *sharper* form than "low": low **and not improvable by enriching the environment or
  raising competence**, because in this configuration the representation is not learned at all.
- **The coupling** — that evaluator quality is *bounded by* that differentiation — is **untouched**.
  Nothing here measures evaluator quality. V3-EXQ-744a's WEAKENS reading (mean_delta_r2=0.130
  failing the 0.15 floor and the 2xSD gate, C2 monotone rho=0.69; real-but-weak, high-variance)
  stands unaltered. This measurement must not be read as rehabilitating the strong bound.

Scope limits, stated plainly:

1. **Configuration-specific.** "The world encoder is untrained" is a fact about the x724/x734 P0
   protocol, not about the REE encoder in general. Other paths do train it — V3-EXQ-740a's
   `world_feat_decode_r2` rose 0.048 -> 0.245 with maturation, which is only possible if the
   encoder moved. The correct generalisation is: *this* measurement, and DREAMER-V3-P-008's, were
   taken on a frozen random projection.
2. **740a's 0.245 remains low in absolute terms**, and the trained-encoder ceiling is NOT measured
   here. Whether training lifts the contrast ratio is unmeasured and is the obvious next probe.
3. **The raw channel's own contrast ratio is also flat** across rungs and competence (0.579-0.696).
   So on the contrast statistic the (b)/(c) axes had limited upstream variation to propagate, and
   the flatness of `z_world` CR is on its own weaker evidence than it looks. The discrimination
   rests on the *attenuation factor* and the frozen-weights finding, not on flatness alone. The
   dimensionality channel is where (b)/(c) genuinely did vary upstream (raw PR 3.3x), and there
   `z_world` tracked at ~1/5 amplitude and inverted in 2/8 paired cells.
4. **2 seeds per cell.** Adequate for effects this large (782x vs 1.5x), thin for the
   dimensionality-tracking claim in 3a.

## 6. What this does NOT license

- No build. The `complex (probe-gated)` node is answered as a `puzzle (known rules)` — the missing
  fact has been obtained — but the follow-on ("train the world encoder and re-measure") is a
  separate decision that this diagnostic does not make.
- No bearing on MECH-459 / return-scale / normaliser.
- No bearing on V3-EXQ-780 vs V3-EXQ-781. Neither leg of the GOV-FANOUT-1 discrimination is
  supported or weakened by anything here; both remain `claimed` and the discrimination remains open.
  `mech457_competence_bootstrap_explorer` stays `blocked_pending_discrimination`.

## 7. Reproduction

Harness lived in the session scratchpad and is not committed (DREAMER-V3-P-008 pattern):
`zworld_static_probe.py` (manifold grid), `zworld_decode_probe.py` (decodability),
`weight_check.py` (weight-delta). Each imports `x724` / `x734` / `x742` and
`_lib/capability_eval.py` from `ree-v3` and runs under `/opt/local/bin/python3`; total runtime
~1 h wall-clock on the Mac. The manifold grid and decodability passes need no warmup (the warmup
is a provable no-op for the world path, per 3b).
