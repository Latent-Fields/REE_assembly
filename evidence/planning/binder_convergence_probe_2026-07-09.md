# Cross-stream binder convergence probe -- 2026-07-09

**Step 1 of the `cross_stream_binding_substrate` repair** routed by
`failure_autopsy_V3-EXQ-725_2026-07-09`. Diagnostic only; no substrate mutation.
`claim_ids=[]`. Confirms the separability diagnosis BEFORE the full build.

## Setup
Exact 725 env+agent (learned binder, `reef_bipartite_layout=True`, 12x12
CausalGridWorldV2). Collected the observed `(z_self, z_world)` pairs the P0
curriculum feeds (`agent.sense` -> `latent.z_self/z_world`), random-action
exploration (generous separability test; the real P0 uses SP-CEM -- the retest,
not this probe, is the true convergence gate). 720 pairs/seed, 32-dim latents.
Chance floor = `log(batch=64) = 4.159` nats (symmetric-CE InfoNCE).

## Finding 1 -- collinearity is extreme AND buffer-wide (not just consecutive)
| stream | consec-tick cos | buffer off-diag cos (mean / std) |
|---|---|---|
| z_self  | 0.9966 | 0.9889 / 0.0077 |
| z_world | 0.9971 | 0.9886 / 0.0071 |

Nearly every latent in the whole buffer points the same direction. The
dot-product InfoNCE logit is dominated by a near-constant shared **magnitude**;
the residual **directional** conjunction signal (std ~0.007) is drowned. This is
why raw InfoNCE cannot leave chance. (Step-deltas are far less collinear:
dz_world off-diag cos = 0.011, dz_self = 0.223.)

## Finding 2 -- the unlock is L2-normalizing the projections (cosine InfoNCE)
Fresh phi_self/phi_world per construction, 1200 steps (seed 42):
| construction | final | frac of chance | converged? |
|---|---|---|---|
| A raw within-tick (**CURRENT**) | 3.694 | 0.888 | flat (no) |
| B cosine (L2-norm proj) | 3.195 | 0.768 | **yes** |
| C delta (phasic), raw dot | 3.850 | 0.926 | no |
| D delta + cosine | 3.212 | 0.772 | yes |
| E variety-filtered, raw dot | 3.764 | 0.905 | no |
| F variety + cosine | 3.163 | 0.761 | yes |

**Every converging construction has `cosine=True`.** Delta / variety alone do NOT
help (raw dot still magnitude-dominated); they add nothing over plain cosine.

## Finding 3 -- cosine converges across seeds; temperature tunes the margin
1500 steps, seeds 42/43/44 (final loss / frac-of-chance; CONV = frac<0.90):
| config | s42 | s43 | s44 | CONV all |
|---|---|---|---|---|
| cosine bd16 T0.5 | 0.765 | 0.776 | 0.804 | yes |
| cosine bd16 **T0.2** | **0.652** | **0.657** | **0.682** | **yes** |
| cosine bd16 T0.1 | 0.577 | 0.639 | 0.652 | yes |
| cosine bd32 T0.2 | 0.628 | 0.656 | 0.696 | yes |
| cos+delta bd32 T0.2 | 0.642 | 0.643 | 0.676 | yes |
| cos+variety bd32 T0.2 | 0.622 | 0.667 | 0.691 | yes |

## Verdict
**SEPARABLE -- repair is viable and is a curriculum/geometry change, not an
environment swap.** The environment already carries enough conjunction signal;
the binder was throwing it away by scoring un-normalized projections.

## Chosen repair (minimal, sufficient)
1. L2-normalize `h_self`/`h_world` before the InfoNCE dot in `learn_step`
   (and in `binding_score`, so the rebinding probe reads the same geometry the
   loss trained). Learned-path only; fixed mode byte-identical.
2. Retest sets `temperature=0.2` (bd16 default) for a robust ~0.65 margin.
3. Expose `binder_converged = smoothed_last_loss < CONV_FRAC*log(batch)`
   (CONV_FRAC default 0.85 -- cleanly rejects the raw flat-at-0.89 path).
4. NOT adopted: delta / variety-filter (no gain over cosine), bind_dim change.
