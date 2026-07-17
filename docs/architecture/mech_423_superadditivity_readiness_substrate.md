---
title: MECH-423 Super-Additivity Readiness Substrate (R1 / R2 / R3)
parent: "Roadmap & Planning (V4+)"
grandparent: Architecture
nav_order: 2
status: provisional
status_asof: 2026-07-17
status_claim: MECH-423
---

# MECH-423 Super-Additivity Readiness Substrate (R1 / R2 / R3)

**Status:** IMPLEMENTED 2026-06-12
**Claim:** MECH-423 (cross-model super-additivity) -- this substrate does NOT
promote MECH-423; it makes the EXP-0380 readiness readouts measurable so the
super-additivity ablation can be queued.
**Amends:** ARC-004 (shared L-space latent / inference machinery) +
MECH-121 (NREM consolidation cluster) -- implementation_note only, no new claim.
**Unblocks:** proposal EXP-0380 (`evidence/planning/manual_proposals.v1.json`),
previously `blocked_substrate`.

## Problem

The EXP-0380 acceptance check gates the super-additivity verdict on a
NON-DEGENERACY / READINESS conjunction (R1 AND R2 AND R3), grounded in the
2026-06-12 lit-pull `evidence/literature/targeted_review_mech_423_integration_prerequisites`:
the integrated arm is only interpretable as evidence about MECH-423 once the
integration machinery is demonstrably doing cross-module work. A
`/queue-experiment` Step-2.5 substrate check (2026-06-12) verified that the R1/R2/R3
readouts the acceptance check requires were ABSENT from the live ree-v3 eval path,
so the ablation would self-route `substrate_not_ready_requeue` on every run (a
vacuous probe) -- hence `blocked_substrate`.

| Readout | What it asserts | Gap (verified 2026-06-12) |
|---|---|---|
| **R1** coupling | `||grad_z|| > 0` in each module AND mean inter-module gradient cosine `>= 0` on the shared latent | no z_shared / retain_grad hook in ree_core (phased detach-training discipline blocks cross-module grad flow into a shared latent) |
| **R2** inference convergence | per-inference-step `||delta z_shared|| < 0.05 * ||z_shared||` (loop converged) | `REEAgent.sense()` calls `latent_stack.encode()` exactly once per tick (`agent.py`): a fixed feed-forward amortized encode, no settling loop, so per-step `||delta z_shared||` has no source |
| **R3** offline interleaving | MECH-121 consolidation updates `> 0` AND cross-module replay share `> 0` AND interleaved (not blocked single-module) schedule | MECH-121 replays REGION-keyed traces with no module identity (`sleep/phase_manager.py:234`); the only offline gradient pass trains `e2_harm_s` ALONE (`phase_manager.py:329`) |

Minimum to make the probe non-vacuous: R2 + R3 (without both, the integrated arm
equals the isolated arm by construction). R1 is constructible inside an experiment
arm and is provided as a small reusable utility so the EXP-0380 arm does not
reinvent it.

## Solution

All three capabilities are behind no-op-default flags, bit-identical OFF, with
contract tests proving it. Pure-arithmetic readouts. MECH-094 simulation-gating
on every replay-sensitive path.

### R2 -- iterative-inference settling readout (ARC-004 machinery)

`ree_core/latent/stack.py` (`LatentStack.encode`). The legacy block is a fixed
two-pass amortized recognition (bottom-up init -> one top-down round). When
`use_iterative_inference=True`, that single round is generalised into a
predictive-coding settling loop over the shared `z_beta -> z_theta -> z_delta`
stack -- iterate the recurrent top-down map with the bottom-up data terms
(`combined_init`, `z_beta_init`, `body_obs`, `world_obs`) held fixed -- run BEFORE
the SD-007 reafference correction + EMA, so the settled instantaneous estimate is
what gets smoothed.

- **Config** (`LatentStackConfig`, no-op defaults): `use_iterative_inference=False`,
  `inference_settle_iters=1`, `inference_convergence_rel_tol=0.05`. Surfaced via
  `REEConfig.from_dims(**kwargs)` (signature-stable kwargs.pop).
- **Readout:** `LatentState.inference_convergence` (plain-float dict:
  `per_step_rel_delta[]`, `converged: bool`, `n_iters: int`, `final_rel_delta:
  float`), cached on `agent.last_inference_convergence`. `detach()` passes it
  through unchanged (no graph).
- **OFF path:** the whole block is skipped (`inference_convergence=None`);
  `settle_iters=1` with the flag on runs zero extra rounds -> latent values
  byte-identical to legacy.
- **Grounding:** Gershman & Goodman 2014 (amortized inference; the amortization
  gap makes "converged" measurable). EXP-0380 R2 reads `final_rel_delta < 0.05`.
- **Activation smoke (2026-06-12):** OFF bit-identical; ON (settle_iters=8,
  rel_tol=0.02) settles in 3 rounds, per-step delta 0.062 -> 0.0074, converged=True.

### R3 -- module-tagged interleaved cross-module consolidation (MECH-121 cluster)

`ree_core/sleep/cross_module_consolidation.py` (`CrossModuleConsolidator`). Pure
orchestration: takes named modules, each with a loss closure (fresh replay draw)
and its parameter list, runs a configurable schedule, tags each replayed trace by
which modules it actually updated, and reports a flat readout dict.

- **Schedule:** `"interleaved"` runs one gradient step on every module per trace,
  so a trace can touch `> 1` module (the integration regime); `"blocked"` trains
  modules sequentially, so each trace touches exactly one module
  (`cross_module_replay_share == 0` -- the catastrophic-interference control, NOT
  a bug). A module is "touched" only if its loss is non-trivial (a closure returns
  an exactly-zero sentinel when it has no replay content), so the share genuinely
  reflects whether integration happened.
- **Wiring:** built on the agent (`agent.cross_module_consolidator`) when
  `use_cross_module_consolidation=True` -- usable standalone by the experiment -- and
  passed to `SleepLoopManager`, where a flag-gated hook in `_run_cycle` (after the
  existing writeback, additive) runs the E1 + E2 default loss set sourced from the
  agent's replay buffers (`compute_prediction_loss` / `compute_e2_loss`) and merges
  `cross_module_consolidation_*` keys into the sleep-cycle metrics -- so the readout
  is a readout of the LIVE MECH-121 pipeline.
- **Config** (`REEConfig`, no-op defaults): `use_cross_module_consolidation=False`,
  `cross_module_consolidation_schedule="interleaved"`,
  `cross_module_consolidation_steps=0` (0 == none), `..._lr=1e-3`, `..._batch=16`.
- **MECH-094:** the SAME explicit exception the `e2_harm_s` writeback uses -- a
  weight-update pass with per-module optimisers constructed LOCALLY over only the
  named modules' parameters; nothing is written to residue / anchors / memory. A
  `simulation_mode` guard returns the zeroed readout (no-op); the legitimate offline
  call site passes `False`.
- **OFF path:** consolidator not built (`None`); `_run_cycle` unchanged -> bit-identical.
- **Grounding:** McClelland/McNaughton/O'Reilly 1995 + Kumaran/Hassabis/McClelland
  2016 (interleaving is necessary for shared-representation integration; a blocked
  schedule -> catastrophic interference -> sub-additive artefact). EXP-0380 R3 reads
  `n_updates > 0 AND cross_module_replay_share > 0 AND interleaved == True`.
- **Activation smoke (2026-06-12):** OFF consolidator None; interleaved share=1.0
  / interleaved=1.0 / 8 updates; blocked share=0.0; sim no-op; live sleep-cycle
  `force_cycle` merges the keys with share=1.0.

### R1 -- shared-latent gradient probe (reusable utility)

`ree_core/utils/shared_latent_probe.py` (`shared_latent_gradient_probe`). A small
pure function: given a shared latent and a `{module: loss_fn(z_shared)}` map, it
computes `d(loss)/d(z_shared)` per module via `torch.autograd.grad(...,
retain_graph=True)` and returns `{per_module_grad_norm, min_grad_norm,
mean_pairwise_cosine, n_modules, coupled}`. No substrate state, no hot-path touch.
EXP-0380's integrated arm constructs `z_shared` (the latent fed jointly to E1+E2)
and calls this for the R1 verdict (`min_grad_norm > 0 AND mean_pairwise_cosine >=
0`). Grounding: Yu/PCGrad 2020 (conflicting gradients = negative transfer) +
Caruana 1997 (shared-rep MTL beats isolated only when tasks are related).

## What this enables

EXP-0380 (the 3-arm ISOLATED / INTEGRATED-PAIR / INTEGRATED-TRIPLE super-additivity
ablation) can now be queued: its pre-registered R1/R2/R3 readiness gate reads
`agent.last_inference_convergence` (R2), the sleep-cycle / standalone
`cross_module_consolidation_*` metrics (R3), and `shared_latent_gradient_probe`
(R1) before scoring super-additivity. The substrate does NOT change MECH-423's
status (still candidate, experimental_confidence 0.0); it only removes the
`blocked_substrate` gate.

## Validation

Contract tests: `tests/contracts/test_mech423_inference_convergence.py` (R2),
`tests/contracts/test_mech423_cross_module_consolidation.py` (R3). Substrate-readiness
validation experiment: queued via `/queue-experiment` (claim-free diagnostic;
asserts R2 converges + R3 interleaved share>0 vs blocked share=0 + R1 coupling).
Full ree-v3 contract suite green with all flags OFF (bit-identical).

## Related

MECH-423, ARC-004, MECH-121, ARC-001/002 (E1/E2 streams), MECH-081/082/033
(pairwise transfer paths the super-additivity claim generalises), ARC-080 (object
spine, the triple arm), MECH-273 / SelfModelAggregator (the single-module
`e2_harm_s` offline pass this generalises to E1<->E2), MECH-094 (call-site scoping).
Lit: `evidence/literature/targeted_review_mech_423_integration_prerequisites`.
