---
title: "SD-078: common-mode-invariant (centered) CandidateRuleField context key"
nav_exclude: true
status: candidate
status_asof: 2026-07-24
status_claim: SD-078
---

# SD-078: policy.common_mode_invariant_candidate_rule_field_context_key

**Claim ID:** SD-078
**Subject:** policy.common_mode_invariant_candidate_rule_field_context_key
**Registered:** 2026-07-22
**Status:** IMPLEMENTED (2026-07-22)
**Depends on:** ARC-063 substrate (`CandidateRuleField`, ree-v3 `ree_core/policy/candidate_rule_field.py`), SD-008 (z_world differentiation -- the deficit this works around), SD-066 and SD-077 (the same fix, previously validated on two other consumers)
**Blocks:** ARC-063 GAP-B (the differentiated rule pool), MECH-262 / SD-033a rule_state differentiation, the V3-EXQ-654 lineage

## Problem

The ARC-063 `CandidateRuleField` keys three decisions on a raw `z_world` context:

1. **mint-block** -- `_cosine(context, rule.context_tag) >= mint_block_thresh`
2. **recurrence bucket** -- `_context_bucket()`, the sign pattern of the leading
   8 dims (an absolute threshold at zero)
3. **gate retrieval** -- `_cosine(context, r.context_tag) >= match_thresh`

Under the SD-008 `z_world` under-differentiation every context sits inside one
narrow common-mode cone, so all three measure the encoder's shared offset rather
than the context.

Measured 2026-07-22 (session `sad-newton-00451d`) by driving the real module over
the real V3-EXQ-669b Stage-0 nursery context stream (`CausalGridWorldV2(size=8,
num_hazards=0, num_resources=6, use_proxy_fields=True)`, 160 contexts, seed 101,
`alpha_world=0.9`):

| context source | pairwise cosine min / mean | fraction of pairs < 0.8 |
|---|---|---|
| raw `world_obs` (control) | 0.3000 / 0.6859 | 60.2% |
| `z_world` (the default key) | **0.9767** / 0.9928 | **0.0%** |
| `e2.world_forward(z_world, a)` (the 654b amend's key) | **0.9426** / 0.9887 | **0.0%** |

and the resulting decision statistics, from the module itself:

| arm | n_minted | max live rules | `max_pairwise_rule_dist` | distinct buckets |
|---|---|---|---|---|
| raw `z_world`, mature dynamics | **1** | **1** | **0.0000** | **1** |
| raw `z_world`, legacy dynamics | 1 | 1 | 0.0000 | 1 |
| `e2.world_forward` context | **1** | **1** | **0.0000** | 2 |
| centered `z_world` (this SD, in-module) | **9** | **9** | **1.7011** | 20 |

**The pool is structurally capped at ONE rule.** With every pairwise context
cosine above ~0.94, the mint-block fires against the first minted rule for every
subsequent context at any threshold the config can express. `n_minted` is
nonetheless large in the 654b runs because rules *retire* and a lone re-mint then
succeeds against an empty pool -- mint 1, block all, retire, re-mint. That is
exactly the "churn" the V3-EXQ-654b/654d autopsies described, and
`crf_max_pairwise_rule_dist == 0.0` in every ARM_ON cell is not a churn symptom
but a **tautology**: the metric needs two concurrent rules and there can never be
two.

### Why the two existing mitigations cannot work

Both were aimed at this exact symptom by the 654b amend, and both are measured
ineffective. They are deliberately **left in place** (no default changes), but
should not be re-tuned as the fix:

- **`mature_mint_block_threshold` raised to 0.8.** The block fires whenever a
  context is within the threshold of an existing tag; the *lowest* observed
  pairwise cosine is 0.9426. No threshold below that clears it, and a threshold
  above it would be slicing the untrained encoder's numerical residue. Pinned as
  contract C3 across the whole expressible range [0.5, 0.94] so the wrong lever
  cannot be silently re-attempted.
- **`crf_context_from_e2_world_forward`.** Its docstring calls this "the
  structural relief" for "low raw-z_world spread". It is not: the predicted
  next-`z_world` carries the same offset (min cosine 0.9426 vs z_world's 0.9767),
  and the field still mints exactly one rule with `dist = 0.0000`. It routes to a
  different point inside the same cone.

## Solution

Apply the **SD-066 / SD-077 pattern** to `CandidateRuleField`: maintain a slow EMA
**common-mode baseline** of presented waking contexts and take every cue
comparison on the **centered residual** `context - baseline`. Entirely internal to
`ree_core/policy/candidate_rule_field.py` plus one `getattr` in the agent's config
build -- no data-flow change.

- **Baseline** (`_baseline`): EMA at `cue_baseline_alpha` (default 0.02, matching
  SD-066/SD-077 -- `z_world` is a per-tick encoding, not an integrator).
  **Lazily seeded** from the first waking context, so there is no zero-init
  cold-start transient.
- **Advanced in `step()`** before any cue arithmetic, so mint-block, bucket and
  gate all read the same residual within a tick.
- **MECH-094:** `simulation_mode` ticks never advance the baseline (`step()`
  already returns before the advance on that path; `observe()` re-checks so it is
  safe to call directly).
- **Tags are stored RAW and centered at comparison time** -- a drifting baseline
  then moves query and every stored tag together and can never leave the pool
  internally inconsistent (SD-077's rationale, same trade).
- **The recurrence bucket is centered too.** It is a sign pattern, i.e. an
  absolute threshold at zero, and is common-mode dominated in exactly the way the
  cosines are (1 bucket raw vs 20 centered). Centering only the cosines would fix
  the mint-block while leaving the recurrence counter unable to tell regimes
  apart.
- **The baseline PERSISTS across `reset()`.** It is cue geometry, not rule
  content; the encoder's offset does not reset when the episode does.

### Config

| Param | Type | Default | Purpose |
|---|---|---|---|
| `CandidateRuleFieldConfig.cue_centering` | bool | `False` | master switch; OFF allocates no baseline and runs no baseline arithmetic |
| `CandidateRuleFieldConfig.cue_baseline_alpha` | float | `0.02` | common-mode EMA rate |
| `REEConfig.crf_cue_centering` | bool | `False` | `from_dims` knob (all three plumbing sites) |
| `REEConfig.crf_cue_baseline_alpha` | float | `0.02` | `from_dims` knob |

**Backward compatible.** With `cue_centering=False` the OFF path is bit-identical:
`observe()` returns immediately, `_centered()` is the identity, and no baseline
tensor is allocated. Verified by contract C1 and by end-to-end agent smoke
reproducing the 654b signature exactly (`n_minted=1`, `dist=0.0000`) on three
seeds.

**Phased training: not required.** `CandidateRuleField` is a pure stateful tensor
store -- no `nn.Module`, no trainable parameters, no gradient flow. SD-078 adds one
non-trainable tensor.

## Architecture Context

This is the **third** consumer to need this fix, after SD-066 (the SD-051
`ConditionedSafetyStore` release gate) and SD-077 (the MECH-189
`SuperOrdinalGoalMemory` cue key), and it was found by the sweep those two
motivated rather than by a further misleading experiment. A fourth, SD-079
(`Anchor.goal_match` on `z_goal`), was found in the same sweep.

Root cause remains SD-008 `z_world` under-differentiation. SD-070 measured that
the prescribed P0 anti-collapse recipe **collapses** `z_world` (participation ratio
~1) rather than repairing it, so the encoder-level fix is unavailable and
consumer-level centering is the correct workaround.

The distinguishing feature of this instance is that the pin had **already produced
two rounds of misdiagnosis**: the 654b and 654d autopsies both read the pinned
statistic as a dynamics problem (retire-churn, then conflict-gate crowding) and
built substantial recalibration machinery for it (`mature_pool_dynamics`,
`availability_maintenance`, the conflict-gate amend). That machinery is not
removed -- it may well be needed once the pool can hold more than one rule -- but
it was never the blocker.

## What This SD Enables

- ARC-063 GAP-B's readiness gate (`crf_max_pairwise_rule_dist > floor` AND
  `crf_frac_active >= 0.30`) becomes reachable: the distance term is no longer a
  tautological zero.
- SD-033a / MECH-262 `rule_state` can be genuinely differentiated rather than
  sourced from a one-rule pool.
- The V3-EXQ-654 lineage's repeated "the pool never matures" finding gets a
  testable alternative explanation.

## Related Claims

ARC-063 (CandidateRuleField), SD-033a (LateralPFCAnalog rule_state consumer),
MECH-262, SD-008 (root cause), SD-070 (why the encoder-level fix is unavailable),
SD-066 + SD-077 + SD-079 (prior/sibling instances of the identical failure mode).
