---
title: "SD-106: Generic Bottleneck Variance Preservation"
parent: "Goals, Drives & Motivation"
grandparent: Architecture
nav_order: 106
status: implemented
status_asof: 2026-09-11
status_claim: SD-106
---

# SD-106: encoder.generic_bottleneck_variance_preservation

**Claim ID:** SD-106
**Subject:** encoder.generic_bottleneck_variance_preservation
**Status:** IMPLEMENTED (2026-09-11; validation owed -- V3-EXQ-1015)
**Registered:** 2026-09-11 (minted by `/governance` gov-20260911; this doc written the same day,
the entry carried `design_doc: null`)
**Depends on:** SD-005 (split encoder), SD-070 (the P0 recipe this extends). No unresolved
prerequisites -- `depends_on_unresolved` is empty on the queue entry.
**Blocks:** SD-015 z_resource pipeline, ARC-030 benefit terrain, MECH-117 wanting/liking approach,
the EXQ-085h..o goal-directed cluster, MECH-457, ARC-065.
**Supersedes in shape:** SD-018 (which supervises ONE NAMED FEATURE; V3-EXQ-978 returned it NULL).
SD-018 remains implemented and is not retired by this entry.

## Problem

The observation->z_world bottleneck is the V3 binding constraint. V3-EXQ-1010 (2026-09-09,
diagnostic PASS, claim-free; confirmed autopsy `failure_autopsy_V3-EXQ-1010_2026-09-11.json`,
REE_assembly `652ababa92`, user-gated, `dry_run_checked=true`) swept DECODER CAPACITY over
~77,000x in parameters against the frozen latent SD-070's P0 recipe produces, holding the
representation, dataset, seeds, held-out split, standardiser and fit protocol fixed.

- Frozen trained latent: best-over-capacity held-out oracle-action agreement
  **0.6839 / 0.6846 / 0.6656** -- 0/3 seeds clear the pre-registered 0.80 bar.
- The SAME ladder on the SAME latent memorises the training split at **0.9996-0.9998**, so the
  null is not an under-powered reader.
- **PCA-32** of the encoder's own 250-dim input at the encoder's own 32-dim width clears both
  thresholds **3/3** at 0.8836 / 0.8729 / 0.8763, so the protocol is sound.
- The same architecture at **RANDOM INITIALISATION** scores **0.7155 / 0.6895 / 0.7084** -- at or
  ABOVE the trained latent on 3/3 seeds.

Verdict `H-F-content-discarded-at-encode`: CONFIRMED. Training contributes nothing positive at
any reader capacity. The repair is at the ENCODER'S OBJECTIVE, not the consumer. Not width, not
consumer capacity, not consumer learning (H-B eliminated at V3-EXQ-1002).

V3-EXQ-1008's consumer-rung decomposition of the 0.1998 PCA-to-trained gap splits it as
**-0.0959** (what fitting a linear projection FOR VARIANCE PRESERVATION buys) / **-0.0779** (what
the encoder's nonlinear architecture costs at random init) / **-0.0260** (what REE's objective
costs on top). The single largest term is a preservation pressure neither the architecture nor
the objective contains.

### Why the existing reconstruction leg does not supply it

`ZWorldP0Config` already carried `reconstruction_weight=10.0`, so the missing piece was not a
missing term. Measured on the x724 rung after a full run of the shipped recipe:

| term | weight | raw | contribution | share |
|---|---|---|---|---|
| variance hinge | 25 | 0.712 | 17.79 | 80.3% |
| covariance | 50 | 0.041 | 2.07 | 9.3% |
| 4 grounding CE heads | 1 each | -- | 2.11 | 9.5% |
| reconstruction | 10 | 0.0177 | **0.177** | **0.80%** |

VICReg anti-collapse is 90% of the objective and reconstruction 0.8% of it. The leg is on the
WRONG SCALE, not under-weighted: raw MSE against a sparse one-hot-dominated observation is
~0.018, where the hinge and CE terms it competes with are O(1) by construction. Consequently the
trained latent retains linear-decodable `world_obs` content at R^2 0.9652 against PCA-32's
0.9984 -- **~22x more input variance discarded**, with PCA-32 explaining 99.84% of `world_obs`
(so a 32-dim code can be near-lossless here; the objective simply never asks for it).

## Solution

Two additions to the P0 path, both no-op by default.

1. **Scale-normalised preservation term** -- `ZWorldP0Config.preservation_weight` (default
   `0.0`). Adds `preservation_weight * MSE(_preserve_head(z_world), world_obs) / var_bar`, where
   `var_bar` is the TRAIN SPLIT's mean per-element variance of `world_obs` (constant, so the
   denominator adds no gradient noise). The term is therefore fraction-of-variance-unexplained
   (`1 - R^2`), O(1) and dataset-scale-free. `_preserve_head` is a dedicated `nn.Linear(world_dim,
   world_obs_dim)`, not shared with `_recon_head`: a separate module keeps the OFF path provably
   untouched. It is LINEAR on purpose -- with a linear decoder the MSE optimum IS the principal
   subspace (Baldi & Hornik 1989), the same object the acceptance target names as its anchor.

2. **Zero-initialised linear bypass** -- `LatentStackConfig.use_world_encoder_skip` (default
   `False`). `SplitEncoder.world_encoder` is `Linear(world_obs_dim, 64) -> ReLU ->
   Linear(64, world_dim)`; a ReLU MLP can only approximate the linear variance-preserving map
   PCA-32 realises exactly. Adding `W_skip . world_obs` makes the encoder family CONTAIN it.
   Zero-init (ReZero, Bachlechner et al. 2021) makes enabling the flag a no-op at step 0.
   `ZWorldP0Trainer.world_path_parameters()` includes it, so it is actually trained and the
   V3-EXQ-783 weight-delta readiness check still sees the whole world path.

Files: `ree-v3/ree_core/latent/zworld_p0.py`, `ree-v3/ree_core/latent/stack.py`,
`ree-v3/ree_core/utils/config.py`.

### Measured effect (2 seeds; proxy DVs)

Linear-decodable `world_obs` R^2 / `resource_field_view` R^2 -- the 25-dim field slice the 1010
autopsy reports decodes the oracle at 0.9735-0.9832 from raw, hence its use as the proxy:

| recipe | obs R^2 (s42/s43) | resource-field R^2 (s42/s43) |
|---|---|---|
| PCA-32 **anchor** | 0.9983 / 0.9984 | **0.9878 / 0.9894** |
| shipped | 0.9432 / 0.9493 | 0.9264 / 0.9479 |
| preservation 50 + skip | 0.9962 / 0.9962 | 0.9813 / 0.9841 |
| **preservation 200 + skip** | **0.9974 / 0.9978** | **0.9857 / 0.9908** |

SD-070's anti-collapse gate survives (participation ratio 14.68 -> 13.86 against a >= 2.0 gate).

**The cost, stated rather than buried.** At a realistic P0 step count (600 steps, 4000 buffered
observations) mean held-out grounding lift falls 0.5702 (shipped) -> 0.4313 (w=50) -> 0.4064
(w=200) -> 0.3982 (w=500). Lift stays strongly positive so SD-070's gate holds, but roughly a
quarter of the grounding signal is traded for the preservation gain, and the resource-field gain
above w=50 is small. If a downstream consumer depends on grounding discriminativeness rather
than on preserved variance, w=50 is the better operating point.

## Architecture Context

SD-005 splits the encoder; SD-070 supplies the P0 recipe that stops z_world COLLAPSING; SD-106
supplies the pressure that stops it DISCARDING. SD-009 and SD-018 are the two named-feature
supervision attempts that preceded it -- SD-009's target proved unlearnable from the channel it
was wired to, and SD-018's returned NULL at V3-EXQ-978. The reframe this entry rests on, from
the 1010 autopsy's own fan-out note, is that the build is not "fix the objective OR fix the
architecture" but "introduce a bottleneck preservation pressure at all".

## What This SD Enables

SD-015, ARC-030, MECH-117, the EXQ-085h..o goal-directed behaviour cluster, MECH-457, ARC-065 --
all gated behind the observation->z_world binding constraint. **SD-106 PROMOTES NOTHING on its
own**, and no claim in `claims.yaml` yet declares `depends_on: SD-106`, so no `v3_pending` flag
moves on this landing.

## Validation

**ACCEPTANCE TARGET (pre-set by governance, not invented here):** the observation->z_world latent
reaches PCA-32 parity -- `>= 0.85` held-out oracle-action agreement at the consumer rung
(`x734.PPOPolicyNet` at `PPO_TRUNK_HIDDEN`) on a seed majority -- re-measured by re-running
`ree-v3/experiments/v3_exq_1010_zworld_overcapacity_decoder_sweep.py` **UNCHANGED**. The harness,
dataset recipe, calibration anchor and negative control all already exist and need no new build.
Queued as **V3-EXQ-1015**.

Phased training: P0 only, unchanged from SD-070 -- P1 must train on stop-gradient z_world with
the encoder optimiser NOT stepped (EXQ-166b/c/d).

MECH-094: not applicable -- trains an encoder on live observations and writes nothing to memory
during any non-waking state.

## Related Claims

SD-018, SD-070, SD-005, SD-009, SD-015, ARC-030, MECH-117, MECH-457, ARC-065, INV-088, INV-104.
