# MECH-060/067 Write-Locus Contamination Ablation — FAIL (2026-02-27T08:58:22Z)

## Genuine ree-v1-minimal Evidence

**Substrate:** ree-v1-minimal gridworld 10×10, 4 hazards, 5 episodes × 1 seeds × 3 conditions.
**Architecture epoch:** ree_v1_minimal_genuine_v1

## Result

| Condition | Last-quarter harm | Total residue | |attr_corr| (E1 loss vs harm) |
|-----------|-------------------|---------------|----------------------------------|
| FULL (clean write loci)        | 1.5 | 5.9 | 0.055 |
| CONTAMINATED_DURABLE (E1 leak) | 0.5 | — | 0.4115 |
| CONTAMINATED_RESIDUE (pre-commit residue) | 1.3 | 120.3864 | 0.5284 |

- Residue inflation criterion (CONT_RES residue > FULL * 1.1): **PASS**
- Harm ordering criterion (FULL harm ≤ max(contaminated) * 1.05): **FAIL**
- Overall verdict: **FAIL** (partial_support=True)

## Architectural Interpretation

MECH-060 and MECH-067 assert that write-locus separation between the pre-commit channel
(E2 simulation errors) and the post-commit channel (realized env harm) is load-bearing.
This experiment tests what happens when those boundaries are violated.

**Write-locus architecture in ree-v1-minimal (FULL condition):**
- E1 (world model) receives gradients only from `compute_prediction_loss()`, which replays
  actual observed latent states. Pre-commit E2 harm predictions do NOT touch E1.
- Residue field receives harm only via `update_residue(env_harm)` after `env.step()`.
  Pre-commit E2 speculation does NOT accumulate in the residue terrain.

**CONTAMINATED_DURABLE**: E2 prediction error scales the E1 gradient each episode,
modelling pre-commit simulation errors leaking into the durable world model. This
decouples E1 loss from actual observation fidelity, degrading attribution reliability.

**CONTAMINATED_RESIDUE**: `update_residue(-e2_pred)` is called pre-commit, then
`update_residue(env_harm)` post-commit. Pre-commit predictions inflate the residue
field — the terrain accumulates harm from states the agent has not yet visited,
miscalibrating the hippocampal-analogue path weighting.

**Attribution correlation (|attr_corr|)**: Pearson correlation between per-episode E1 loss
and per-episode realized harm. In FULL, E1 trains only on actual observations → E1 loss
should track harm. Contamination should degrade this correlation. Reported for
calibration; not a formal PASS criterion at 200-episode scale.

## Status Implication

FAIL/PARTIAL: One or both contamination signals not detectable at ree-v1-minimal scale. Informative baseline — may require more complex substrate or longer training to reach threshold. Do not demote: architecture is unchanged, substrate resolution is the limiting factor.
