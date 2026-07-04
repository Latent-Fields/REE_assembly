# SD-063 — E2 conditional predictive-uncertainty head

**Claim:** SD-063 (design_decision, candidate, implementation_phase v3, v3_pending)
**Instantiates:** MECH-059 (confidence channel distinct from residual error)
**Depends on:** MECH-059, SD-031
**Motivating diagnostic:** `v3_exq_712_distributional_world_forward_heads_20260704T014207Z_v3`

## Decision

E2's world-forward should carry a **conditional predictive-uncertainty head** that
emits a per-input predictive spread tracking realized error, rather than relying
only on E3's running-variance EMA. The current E2 forward is a point predictor
trained on MSE (`ree-v3/ree_core/predictors/e2_fast.py`, `e2_world.py`); the sole
uncertainty signal is the E3 running-variance EMA, a temporally-smoothed *global*
estimate whose predicted uncertainty has near-zero per-point error correlation
(`precision_error_corr ~ 0.0` by construction). A conditional head lets E3 gate
action commitment on where *this* prediction is uncertain rather than on a running
average — the concrete realization of the MECH-059 confidence channel.

## Preferred form: distribution-free quantile / pinball

The V3-EXQ-712 diagnostic held the encoder + transition set fixed and swapped only
the E2 forward head + loss across four formulations, scoring on the same held-out
`(z_world_t, a_t) -> z_world_{t+1}` transitions (5 seeds, 4760 test transitions):

| Head | CRPS (lower=better) | precision_error_corr |
|------|--------------------|----------------------|
| `quantile_pinball` (winner) | **0.00486** | **0.379** |
| `mse_point` (baseline) | 0.00514 | 0.0 |
| `mixture_gaussian` | 0.00682 | 0.038 |
| `hetero_gaussian` | 0.00708 | 0.040 |

Best distributional CRPS beat point CRPS on 4/5 seeds. The load-bearing finding is
narrow: **only** the distribution-free quantile head helped; imposing a Gaussian
shape (hetero, mixture) on the next-state predictive distribution did *worse* than
the point baseline. The quantile head also delivered a genuine per-point error
signal (0.379) that the EMA cannot carry.

## Caveat (SD-031 dependency)

E2 is an agency detector via the `z_world_observed - E2_world(z_world, a)` residual
(SD-031). A predictive-variance head can absorb the agent-caused component of
next-state variance into "expected spread," quietly killing the agency signal. Any
implementation must show the head does **not** explain away the E2WorldForward
agency residual.

## What v3_pending gates on

SD-063 registers the design insight; it is **not** validated. The diagnostic trained
detached heads (effectively single-phase P1). Promotion requires a real
`/implement-substrate` build wiring a conditional-uncertainty head into E2, plus a
validation experiment showing (a) the CRPS / precision-error-corr advantage survives
joint training, and (b) the SD-031 agency residual is preserved.
