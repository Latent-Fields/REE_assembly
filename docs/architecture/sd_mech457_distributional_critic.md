---
title: "SD-MECH457-DISTRIBUTIONAL-CRITIC: action_learning.distributional_value"
parent: "Goals, Drives & Motivation"
grandparent: Architecture
nav_order: 23
---

# SD-MECH457-DISTRIBUTIONAL-CRITIC: action_learning.distributional_value

**Claim ID:** SD-MECH457-DISTRIBUTIONAL-CRITIC
**Subject:** `action_learning.distributional_value`
**Status:** IMPLEMENTED
**Registered:** 2026-07-18
**Implemented:** 2026-07-18
**Depends on:** MECH-457 actor-critic substrate (`sd_actor_critic_action_learning`) -- IMPLEMENTED
**Blocks:** hypothesis `H-retention-critic` (`evidence/planning/hypothesis_space_registry.v1.json`,
question `competence_floor`); substrate_queue entry `mech457_distributional_critic`
**Portfolio design doc:** `evidence/planning/mech457_retention_portfolio_2026-07-18.md`

## Problem

The MECH-457 campaign's question shape changed at V3-EXQ-780. Its `raw_view` arm reached
**20.933** foraging competence -- the first supra-lift-target (13.05) observation in the whole
campaign -- and RL refinement then **eroded** it to 11.667. The open question stopped being
"which mechanism produces competence" and became "why is produced competence not retained".

V3-EXQ-782 R-(b) supplies the leading, **measured** mechanism candidate: the shared CTRL critic
is flat and uninformed.

| Reading | Measured | Threshold |
|---------|----------|-----------|
| `std(V) / std(G)` | **0.041** | 0.25 (collapse threshold) |
| pre-reward-vs-far separation ratio | **0.016** | 0.25 (floor) |

An uninformed baseline yields an unbaselined, high-variance advantage, which is exactly the
signature that drifts a policy off an installed prior. The substrate could not test this: the
critic was scalar-only (`ActorCriticPolicy.value_head = nn.Linear(hidden, 1)`,
`ree_core/action_learning/actor_critic.py:110`, decoded `:147`) with a scalar-MSE loss at four
`_lib` sites, and there was **no** distributional machinery anywhere in the tree (zero hits for
`twohot` / `two_hot` / `hl_gauss` / `value_bins` / `atoms` / `symlog` in `ree_core/` or
`experiments/`). `/queue-experiment` Step 2.5 stopped all four retention legs on that basis and
nothing was queued.

**The successor-feature escape hatch was checked and fails.** `use_sf_critic`
(`actor_critic.py:116-125`) looks like a built alternative value estimator. It is not usable: it
is hard-wired `False` on every MECH-457 path (`mech457_fanout.py:153,335`;
`mech457_explorer_classes.py:830`), has no field in `BootstrapExplorerConfig`, and its
psi-Bellman + reward-regression losses exist **only** in
`experiments/v3_exq_742_mech457_actor_critic_onoff.py:357-372` -- nothing in `_lib` computes
them. Flipping the flag without porting that block leaves `reward_w` at zero-init and
`V_SF` identically 0: an **untrained** critic read as an alternative one, i.e. a degenerate arm
masquerading as a scientific verdict. This SD therefore builds the distributional critic rather
than reusing the SF one.

## Solution

A new value-estimator form, selected by config, orthogonal to `use_sf_critic`.

**New module** `ree_core/action_learning/distributional_value.py`:

- `symlog(x) = sign(x) * log(1+|x|)` / `symexp` -- compress a wide-dynamic-range return onto a
  bounded support.
- `ValueBins(n_bins=41, limit=10.0, sigma_ratio=0.75)` (`nn.Module`, registered buffers so the
  support moves with `.to(device)`):
  - `project(returns) -> [B, n_bins]` -- two-hot when `sigma_ratio == 0`, otherwise the HL-Gauss
    discretised Gaussian (mass per bin from erf CDF differences over the bin edges, renormalised
    over the finite support, with a one-hot fallback at the nearest end for astronomically
    out-of-support targets).
  - `decode(logits) -> [B]` -- `symexp(E_p[support])`.
  - `cross_entropy(logits, returns)` -- projection computed under `no_grad` (it is a target).

**`ActorCriticPolicy`** (`ree_core/action_learning/actor_critic.py`):

- New ctor args `use_distributional_critic=False, n_value_bins=41, value_bin_limit=10.0,
  value_bin_sigma=0.75`. ON: `value_head = nn.Linear(hidden, n_bins)` + a `ValueBins`.
- `forward()` keeps its 4-tuple signature and still returns a **scalar** `value` (the
  expectation-decode). New `_forward_full()` / `forward_value_logits()` expose the bin logits.
- `ActorCriticStep` gains `value_logits: Optional[Tensor] = None` (None on the scalar/SF paths).
- New `critic_loss(value_logits, returns)` -> CE. **Raises** if the distributional critic is not
  enabled, so a mis-wired ON arm fails loudly instead of silently training nothing.

**Config** (`ree_core/utils/config.py`, `ree_core/agent.py:313`): `actor_critic_use_distributional_critic`,
`actor_critic_n_value_bins`, `actor_critic_value_bin_limit`, `actor_critic_value_bin_sigma`.

**Training loops** (`experiments/_lib/`): a single dispatch,
`mech457_fanout.critic_value_loss(policy, value_logits_t, value_t, ret_t)`, replaces the scalar
MSE at all four sites -- `mech457_fanout.py` (raw-view A2C, z_world shaped A2C) and
`mech457_explorer_classes.py` (`train_a2c`, `_prioritized_credit_replay`). It falls back to the
**identical** `AC_VALUE_COEF * 0.5 * (V - G)^2` when the critic is scalar. Each rollout collects
`value_logits` only when the step carries them. `BootstrapExplorerConfig.use_distributional_critic`
(default `False`) is declared in `as_slice()`, so the flag lands in the arm fingerprint's
`config_slice`.

Out of scope by design: the H-curriculum goal-conditioned trainer
(`mech457_explorer_classes.py:952`) keeps its scalar critic -- it is a different mechanism leg,
not part of the retention portfolio.

### Data flow

```
GAE return G_t (reward-std-scaled)
    -> ValueBins.project      (symlog -> clamp -> HL-Gauss / two-hot)   [target, no_grad]
    -> cross-entropy against value_head(h)                              [the critic loss]
value_head(h) [B, n_bins]
    -> ValueBins.decode       (softmax -> E[support] -> symexp)
    -> ActorCriticStep.value  (SCALAR)
    -> GAE / bootstrap value / credit-replay TD priority / eval         (all unchanged)
```

### Anti-alias constraint (load-bearing)

This build changes what the baseline **knows**. It does not constrain how far the policy may
**move**. `policy_loss`, the log-prob, the entropy bonus, the advantage weighting, the BC
auxiliary and the credit-replay policy term are byte-identical on both branches. That locus --
the update constraint -- belongs to the sibling entry `mech457_policy_kl_anchor`
(`H-retention-consolidation`); a leg changing both would make **neither** readable.

Contract `test_c2_on_leaves_actor_bit_identical` asserts the trunk and policy head are
bit-identical to the scalar arm at the same seed, and `test_c2b` asserts the CE loss produces no
gradient on the policy head. (The shared trunk does receive gradient from the critic term --
exactly as the scalar MSE always has, so this is not a change in the update rule.)

## Architecture Context

`ActorCriticPolicy` now selects among three critic forms: plain scalar (cand-A), successor-feature
(cand-B, `use_sf_critic`), and distributional. The third is **orthogonal** to the first two: it
replaces how the plain value head is parameterised and trained, and is not combinable with the SF
critic (the SF branch returns early and carries no `value_logits`).

## Biological grounding

A ventral-striatal value critic taught by a dopaminergic reward-prediction error is not committed
to a point estimate. Distributional coding of value is the better-supported reading of
dopaminergic populations -- **Dabney et al. 2020**, "A distributional code for value in
dopamine-based reinforcement learning": individual dopamine neurons carry heterogeneous reversal
points that jointly encode a *distribution* over reward rather than a single mean. The scalar
head was the simplification; this is the less simplified form, not an ML import.

## ML/AI engineering notes (Layer 7 -- counsel, not authority)

| Item | Engineering problem it solves | REE adaptation |
|------|-------------------------------|----------------|
| symlog two-hot bins (Hafner et al. 2023, DreamerV3) | Scalar regression onto a heavy-tailed, wide-dynamic-range return collapses to its conditional mean -- precisely what 782 R-(b) measured at `std(V)/std(G)=0.041` | Support sized for the reward-std-scaled GAE returns this loop produces (`limit=10` in symlog space covers magnitudes to ~2.2e4, far beyond them) |
| HL-Gauss target (Farebrother et al. 2024, "Stop Regressing") | A discretised-Gaussian target outperforms two-hot as a value-regression objective | `sigma_ratio` in bin widths, default 0.75 (the paper's recommendation); `0.0` recovers pure two-hot, so both projections are one config field apart |
| Head width kept small (41 bins, 128/256 trunk) | Avoid importing complexity from ImageNet/LLM-scale work | Matches the existing validated 742/734 trunk |

Failure mode defended against: the **degenerate enabled-but-untrained arm** (the SF critic's
actual state). `critic_loss` raises on the scalar path, and contract C5 asserts the CE objective
moves the decoded value onto a known target.

## Phased training

Not required by this SD. The critic head trains inside the existing RL phase on the same returns
the scalar head consumed; it adds no encoder head training on a moving latent target. The z_world
path's existing P0 warmup and `cotrain_encoder` semantics are untouched.

## MECH-094

Not applicable -- no memory writes on simulated or non-waking ticks. This is a loss/decode
transform over the critic head's output.

## Backward compatibility

All new params default to no-op. With defaults: `value_head` is `nn.Linear(hidden, 1)`,
`value_logits` is `None`, and `critic_value_loss` takes the scalar-MSE branch computing the
identical expression. Verified by a full `--dry-run` of
`experiments/v3_exq_780_mech457_bc_prior_discrimination.py` (all six arms, both representations)
and by contracts C1 / C6.

Note: this edits `experiments/_lib/**`, which is bound into `substrate_hash`, so cached
pre-change baseline arm fingerprints correctly refuse reuse across the change.

## What This SD Enables

`H-retention-critic`: BC-install to the raw_view ~20.9 point, then the SAME RL refinement with a
distributional critic vs the current scalar critic, reading the post-installation competence
**trajectory**. Pre-declared null: *the installed prior erodes identically under both critics ->
the critic baseline is not the retention mechanism.*

Per GOV-FANOUT-1, **nothing is queued** until at least two of the four retention legs are
buildable. This SD promotes and demotes no claims; MECH-457 stays `candidate` / `v3_pending`.

## Related Claims

MECH-457 (competence floor), INV-088 (monostrategy representation ceiling), MECH-459.
Sibling substrate entries: `mech457_bc_aux_schedule`, `mech457_policy_kl_anchor`,
`mech457_consummatory_act`.
