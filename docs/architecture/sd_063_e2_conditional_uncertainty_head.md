---
status: provisional
status_asof: 2026-07-10
status_claim: SD-063
---

# SD-063 — E2 conditional predictive-uncertainty head

**Claim:** SD-063 (design_decision, implementation_phase v3)
**Substrate:** built 2026-07-05, disabled-by-default; the V3-EXQ-716 validation falsifier gates any promotion — PROMOTES NOTHING. Governance status is carried by the `status:` frontmatter / claims.yaml.
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

## Implementation (2026-07-05)

Built as a disabled-by-default substrate feature (`/implement-substrate`, session
`implement-sd063-20260705T1724Z`). PROMOTES NOTHING; `v3_pending` stays until the
V3-EXQ-716 falsifier scores.

**Module** — `ree-v3/ree_core/predictors/e2_world_uncertainty.py`:
`E2WorldUncertaintyHead` + `E2WorldUncertaintyConfig`.
- Distribution-free quantile head over `concat([z_world_t, a_onehot])`: 2-layer
  MLP(ReLU) trunk -> `Linear(D*Q)` -> `[B, D, Q]` (matches the V3-EXQ-712 winner;
  `QUANTILE_LEVELS` = 9 levels 0.1..0.9).
- `compute_loss` = pinball / quantile-regression loss.
- `predictive_variance` / `predictive_std` = monotone-rearranged (`torch.sort`,
  anti-crossing) `[q0.1, q0.9]` IQR -> Gaussian-reference variance
  (`IQR_TO_STD_10_90 = 2.5631`), meaned over dims, per batch item, under `no_grad`.
- `z_world_dim` is a REQUIRED constructor arg (no literal default). No `world_dim>=128`
  assert (this is a predictive-spread readout, not the SD-031 discriminative comparator;
  the 712 diagnostic ran at world_dim=32).

**Config** — `LatentStackConfig.use_e2_world_uncertainty` (default `False`;
byte-identical OFF) + `e2_world_uncertainty_hidden_dim` (128) +
`e2_world_uncertainty_lr` (1e-3); `E3Config.use_conditional_precision_gate`
(default `False`). Both surfaced by `REEConfig.from_dims`. Like `use_e2_world_forward`,
the flag signals intent — the head is instantiated at the experiment/agent level, so
`LatentStack.encode()` is untouched (no new `LatentState` field).

**E3 consumer** — `e3_selector.py` `select()` gains `conditional_predictive_variance`
(default `None`). When `use_conditional_precision_gate` is on AND a value is supplied,
the ARC-016 commit decision compares that per-input variance against `effective_threshold`
instead of the state-blind `running_variance` EMA; otherwise it falls back to the EMA
(byte-identical). The `use_harm_variance_commit` path is untouched.

**SD-031 agency-residual guard (structural)** — the head is a SEPARATE `nn.Module`
sharing NO parameters with `E2WorldForward` or the encoder, and its P1 loss reads a
DETACHED `z_world` input AND a DETACHED `z_world_next` target. Its gradients never reach
the forward model that produces the agency residual, so it cannot explain the residual
away by construction. A contract asserts param-disjointness and that a detached target
leaves an encoder-side leaf's `.grad` as `None`. V3-EXQ-716 still confirms preservation
empirically under joint training.

**MECH-094** — does NOT apply (waking online read for commitment gating; no memory
write, no simulation/replay).

**Tests** — 15/15 in `tests/contracts/test_sd063_conditional_uncertainty_head.py`
(config no-op + `from_dims` surface; head shapes + required-dim + level validation;
pinball trains + heteroscedastic conditional variance; SD-031 param-disjoint +
detach-blocks-encoder-grad; E3 gate OFF-ignores / ON-overrides-both-directions /
ON-no-value-EMA-fallback). Full suite 1381/1385 (the 4 fails pre-exist on the clean
base tree, unrelated).

**Validation** — V3-EXQ-716 (`/queue-experiment`), diagnostic falsifier: (a) the head's
per-point predictive variance improves E3 commitment gating vs the EMA
(precision_error_corr > EMA null ~0, CRPS advantage survives joint training), and
(b) the SD-031 agency residual is preserved (head-ON vs OFF within noise). PROMOTES NOTHING.
