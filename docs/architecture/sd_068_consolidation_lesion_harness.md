# SD-068: sleep.consolidation_pipeline_lesion_harness

**Claim ID:** SD-068
**Subject:** sleep.consolidation_pipeline_lesion_harness
**Status:** IMPLEMENTED
**Registered:** 2026-07-17
**Depends on:** SD-017 (offline SWS/REM passes), MECH-120 (SWS denoising), MECH-121 (NREM slot-filling, *held*), MECH-123 (REM precision recalibration), MECH-204 (precision-recalibration consumer)
**Blocks:** the MECH-168 / INV-047 / MECH-169 staged-decline falsifier; a representation-level staged-damage diagnostic (V3-EXQ-778 + power-up V3-EXQ-778a, run 2026-07-17; generative-gain non-vacuity banked offline -- see **Diagnostic results**)

## Problem

The offline-consolidation pipeline exists in the substrate as three phase
operations inside `SleepLoopManager._run_cycle`
(`ree-v3/ree_core/sleep/phase_manager.py`):

| Phase | Claim | Substrate operation |
|-------|-------|---------------------|
| SWS denoising / attractor flattening | MECH-120 | `agent.e1.shy_normalise(decay)` + `run_sws_schema_pass()` |
| NREM episodic->schematic transfer | MECH-121 | `self_model_aggregator.offline_gradient_pass()` / `CrossModuleConsolidator.consolidate()` |
| REM precision recalibration | MECH-123 | `agent.e3.recalibrate_precision_to(target, step)` + `run_rem_attribution_pass()` |

But the cycle exposes only **operational** telemetry (routing counts, replay
diversity, update counts, param-delta). It has **no per-phase output-quality
readout** (denoising-SNR, transfer-fidelity, precision-calibration-error) and
**no per-phase diffuse-damage knob**. Without those two, the distinctive
MECH-168 / INV-047 / MECH-169 falsifier is not buildable on demand:

> Under UNIFORM / diffuse damage across the three phases, does functional failure
> emerge STAGED in reverse dependency order (REM >> NREM >> SWS) rather than
> uniform?

This was adjudicated `blocked_substrate` at IGW-20260717-206 (backlog EVB-0115).
The routing verdict was `/implement-substrate` (build the harness), not another
`/queue-experiment`.

Two hard constraints shaped the design:

1. **Encoding-starvation ceiling.** A design that depends on the agent
   *behaviourally encoding* diverse content to consolidate starves under
   monostrategy collapse -- the confirmed `failure_autopsy_V3-EXQ-538a` lesson
   ("sleep cannot consolidate an unencoded representation"). The only viable path
   is the V3-EXQ-702 **injected-content** precedent: inject known ground truth
   directly onto the substrate and score fidelity against the injection.

2. **Vacuous-pass risk.** Staged decline under uniform damage is vacuous if it is
   merely feed-forward error compounding baked into the DAG topology. The
   genuinely falsifiable content is **error-propagation sensitivity** (does a phase
   amplify or attenuate upstream corruption), which the operational telemetry
   cannot express.

## Solution

An **experiment-layer** harness (no `ree_core` change):
`ree-v3/experiments/_lib/consolidation_lesion_harness.py`.

**Injected-content readouts (702 precedent).** Each phase's operative substrate is
loaded with a known clean signal, then scored against that known signal:

- `sws_denoising_snr` -- inject clean prototypes into `e1.context_memory`, corrupt
  by `sigma`, run SHY, measure SNR of the preserved deviation-structure
  (`10*log10(signal_power / noise_power)`; higher = better). Fully-verified APIs.
- `nrem_transfer_fidelity` -- inject a known per-parameter target (the "replayed
  trace"), run the interleaved `CrossModuleConsolidator` pass, measure the fraction
  of the injected-content gap closed. *Parameter-space proxy* for
  episodic->schematic transfer; substrate-plumbing-fidelity only (see MECH-121
  caveat).
- `rem_precision_error` -- inject a known target precision + starting variance,
  corrupt the reference by `sigma`, run `recalibrate_precision_to`, measure
  `|running_variance_after - 1/target_clean|` (the passthrough (a) baseline).
- `rem_generative_fidelity` -- the clean generative-re-derivation readout (see
  "REM generative gain" below), driven from `rem_precision_error`.

**Uniform diffuse-damage knob.** `diffuse_perturb(t, sigma, gen)` -- additive
isotropic Gaussian scaled to each tensor's own RMS, so a given `sigma` is
comparably severe across phases of different natural magnitude (uniform-in-severity,
not uniform-in-raw-units). One `sigma` applied identically to all three phases ==
the MECH-168/169 "diffuse/uniform damage" model.

**Error-propagation gain (the non-vacuity core).** `error_propagation_gain` sweeps
`sigma` and fits the least-squares slope of each phase's OUTPUT-ERROR (higher =
worse) against `sigma`. Comparing the three *slopes* -- not the raw error levels --
is what separates a genuine staged sensitivity from topology-baked level
differences. REM is measured two ways:

- the bare linear precision nudge (MECH-204) -- **passthrough by construction**;
- the generative re-derivation pass (the hippocampal replay rollout that
  `run_rem_attribution_pass` performs, Hobson & Friston 2012) -- the only locus
  where an attenuating (gain < 1) or amplifying (gain > 1) REM gain can appear.

If the generative gain measures ~ passthrough (~1), the honest diagnostic outcome
is "the V3 REM substrate has no corrective capacity, so its staged-first-failure
is pure topology" -- a valid, informative result, not a harness failure.

### REM generative gain -- rollout-seed injection (`rem_generative_fidelity`)

**(Implemented 2026-07-17; replaces the retired `rem_terrain_variance` proxy.)**
The first cut of the REM (b) leg corrupted the E3 **precision reference** and read
`rem_terrain_variance` back as an amplify/attenuate indicator. But the generative
pass never consumes the precision reference -- it consumes the **rollout seed**
(`theta_buffer.recent`, re-derived through `hippocampal.replay -> e2.rollout_with_world`).
So that read was ~null (confirmed in V3-EXQ-778: PASSED on ree-cloud-4,
`20260717T160320Z`, generative sensitivity ~null).

The clean readout injects the known content onto the seed the generative pass
actually reads:

1. capture `theta_buffer.recent[-1]` (an in-distribution `z_world`) as the known
   clean target;
2. re-derive the **clean** rollout with the exact call `hippocampal.replay` makes
   (`e2.rollout_with_world`), but with a **fixed** action sequence held constant
   across the clean and corrupt re-derivations -- replay's per-call *random*
   actions were precisely why the proxy variance read null (action noise swamped
   the seed effect); `n_rollouts` fixed action draws are averaged;
3. corrupt the seed by `sigma` (the same `diffuse_perturb` primitive) and
   re-derive with the **same** fixed actions;
4. measure the recovered-vs-known-target deviation over the **generated** states
   (`world_states[1:]`, excluding the raw seed passthrough at `t=0`), relative to
   the clean rollout.

The load-bearing number is `rem_generative_gain` = least-squares slope of the
generated-rollout relative deviation vs the injected seed's relative corruption
across the `sigma` grid:

- `gain < 1` -> **attenuating** (genuine generative correction; non-vacuous
  staging -- the REM pass recovers content from a corrupt seed);
- `gain ~ 1` -> passthrough (staging is topology);
- `gain > 1` -> amplifying (MECH-094 psychosis polarity).

Smoke result against the real substrate (seeds 0/1/7, `sigma` in
`{0, 0.25, 0.5, 1, 2}`): `rem_generative_gain` in ~`0.07-0.41`, `attenuates=1.0`
on every seed -- a real, monotone, strongly-attenuating dose-response, no longer
null. The corrupted seed is also pushed into `theta_buffer` and the real
`run_rem_attribution_pass` driven once for liveness telemetry (`rem_n_rollouts`),
confirming the injection point is exactly the seed the live REM path reads;
`rem_terrain_variance` is retained as telemetry only, not scored. This smoke result
is confirmed at n=8 seeds in **Diagnostic results** below (the load-bearing
non-vacuity finding banked into the MECH-168 / INV-047 / MECH-169 staging record).

**Backward-compatible key contract:** `error_propagation_gain` keeps
`rem_generative_output_slope` / `rem_passthrough_calibration_slope` /
`rem_generative_available` (the existing V3-EXQ-778 driver's contract; the
`output_slope` key is now fed by the real readout, not the proxy) and **adds**
`rem_generative_gain`, `rem_generative_gain_mean`, and `rem_generative_attenuates`.

`run_staged_sweep` orchestrates a per-seed sweep and reports the OBSERVED
staged-failure order (phases ranked by gain) versus the predicted reverse-dependency
order `(rem, nrem, sws)`.

**Config:** none added to `ree_core`. The harness builds agents via
`REEConfig.from_dims(..., shy_enabled=True, sws_enabled=True, rem_enabled=True,
use_sleep_aggregation_cluster=True)` -- all pre-existing no-op-default flags.
Backward compatible: no existing experiment's behaviour changes.

## Diagnostic results (2026-07-17)

Two diagnostic legs, reported together (both DIAGNOSTIC / non-scoring; MECH-121
held, NREM leg substrate-plumbing-fidelity only). Neither `error_propagation_gain`
generative-gain key was emitted into a manifest: V3-EXQ-778 ran under the retired
`rem_terrain_variance` proxy (generative sensitivity ~null), and V3-EXQ-778a scores
staging *order* off `calibration_error`/tolerances -- so the generative-gain leg
below is an **offline banking run** of the current harness (ree-v3 `main` `da873a1`,
`rem_generative_fidelity`), 8 seeds `{42, 7, 123, 2024, 99, 7777, 314, 1000}`
(V3-EXQ-778a's seed set, for 1:1 alignment), `sigma` in `{0, 0.25, 0.5, 1, 2}`.

### Leg 1 -- Staging order (V3-EXQ-778a, `...staging_power_diagnostic_20260717T163507Z_v3`, ree-worker-1, PASS/supports)

8-seed damage-tolerance distribution + a 3-way statistical staging test (per-seed
Spearman rho vs predicted `(rem, nrem, sws)`; the two adjacency predictions as
paired tolerance-diff CIs + sign tests; Kendall's W). Verdict label
`staging_seed_variable_underpowered` -- staging match REPORTED, never gated:

- **`nrem` fails before `sws` -- ROBUST.** `sws_tolerance - nrem_tolerance` > 0 on
  **8/8** seeds (mean +0.424, 95% CI [0.422, 0.425], sign-test p = 0.0078). The
  upstream half of the reverse-dependency ordering holds cleanly.
- **`rem` fails first -- CONTESTED / seed-variable.** `nrem_tolerance -
  rem_tolerance` mean -0.097, 95% CI [-0.43, +0.23] straddles 0 (4/8 seeds positive,
  sign-test p = 1.0). The REM-first leg is underpowered at n=8; `rem` tolerance is
  the high-variance phase (std 0.396 vs `nrem` 0.0014, `sws` ~9e-9).
- Overall Spearman mean rho = 0.375 (95% CI [-0.25, +1.00], includes 0); Kendall's
  W = 0.328 (Friedman chi2 = 5.25, df 2). Modal observed order `(rem, nrem, sws)` on
  4/8 seeds.

So the *reverse-dependency staging* is **partially supported**: the NREM-before-SWS
adjacency is robust; the REM-fails-first adjacency is not resolved at this power. All
three phases degrade monotonically with `sigma` (load-bearing C1 PASS, corr >= 0.96
each) and are non-degenerate at `sigma = 0` (P0 control).

### Leg 2 -- REM generative gain (offline banking, current harness, n=8) -- the non-vacuity result

`rem_generative_gain` = least-squares slope of the generated-rollout relative
deviation vs the injected seed's relative corruption. Passthrough leg (bare precision
nudge, MECH-204) is **gain = 1 by construction** (linear full-adoption interpolation
passes corruption straight through):

| seed | `rem_generative_gain` | `rem_generative_gain_mean` | attenuates (gain<1) |
|------|-----------------------|-----------------------------|---------------------|
| 42   | 0.190 | 0.173 | yes |
| 7    | 0.409 | 0.429 | yes |
| 123  | 0.067 | 0.066 | yes |
| 2024 | 0.076 | 0.068 | yes |
| 99   | 0.040 | 0.042 | yes |
| 7777 | 0.212 | 0.218 | yes |
| 314  | 0.077 | 0.083 | yes |
| 1000 | 0.123 | 0.138 | yes |
| **mean** | **0.149** (min 0.040, max 0.409, std 0.121) | **0.152** | **8/8** |

**`rem_generative_gain` = 0.149 mean, 8/8 seeds attenuating (gain < 1), decisively
below the passthrough leg's gain of 1.0.** The `_mean` (per-`sigma` point-gain
average) corroborates the slope (0.152). The per-seed tolerance orderings reproduce
V3-EXQ-778a's exactly (same code + seeds -- a consistency cross-check).

The load-bearing conclusion: **the REM staged-first-failure is NOT pure topology.**
The generative re-derivation pass has genuine corrective capacity -- it attenuates a
diffusely corrupted seed rather than passing it through (gain 1) or amplifying it
(gain > 1, the MECH-094 psychosis polarity). In the harness's non-vacuity vocabulary,
"the correction needs an intact seed": REM's early vulnerability under diffuse damage
reflects a real transfer function, not merely its downstream position in the DAG.

(`rem_passthrough_calibration_slope` -- the raw `calibration_error`-vs-`sigma` slope
in variance units -- ranges 0.03-599 across seeds; it is scale-variable telemetry
under the `step=1.0` full-adoption measurement choice, NOT the dimensionless gain, and
is NOT load-bearing. The by-construction passthrough *gain* is 1.0; the load-bearing
contrast is generative-gain 0.149 << 1.)

### Combined diagnostic reading

Staging order under uniform diffuse damage is **partially confirmed** (NREM-before-SWS
robust; REM-first seed-variable/underpowered), and -- critically -- the piece that
would make even a confirmed staging *vacuous* is refuted: the REM generative pass is
**strongly attenuating (gain ~0.15 << 1 on 8/8 seeds)**, so the pipeline's
staged-decline behaviour rests on a real error-propagation transfer function, not on
feed-forward topology alone. This is DIAGNOSTIC evidence for the *shape* of the
MECH-168 / INV-047 staged-decline prediction (and MECH-169's V3-testable staging
half); it does not promote any claim, and MECH-121 stays held (the NREM leg is
plumbing-fidelity only).

## Architecture Context

The 120/121/123 <-> substrate mapping is **not** a clean 1:1 feed-forward chain in
code (SWS = schema write + SHY; the "NREM slot-filling" content is realised by the
replay / offline-gradient path; REM = attribution replay + precision nudge). The
dependency ORDER is nonetheless real -- REM requires the SWS-installed slots to
exist, and the pass docstrings enforce the call ordering -- which is exactly the
property the staging falsifier needs.

The harness measures each phase's transfer function on a FRESH agent under the same
diffuse damage, deliberately *not* as a single serial pass. A serial pass would
bake in the very error-compounding the non-vacuity contract must avoid.

**MECH-094:** the harness runs weight/state operations offline; it produces no
hypothesis-tagged residue/anchor/memory writes beyond what the phase ops already
do, and does not simulate-then-commit. No new MECH-094 surface.

**Glymphatic half OUT OF SCOPE.** MECH-169 is a complementarity meta-claim; its
glymphatic / amyloid STRUCTURAL-damage half has no V3 analog (no amyloid /
clearance / diffuse-structural-damage substrate). The harness models only the
CONSOLIDATION-side functional consequence of uniform damage.

## What This SD Enables

- A representation-level staged-damage diagnostic (queued via /queue-experiment,
  `EXPERIMENT_PURPOSE="diagnostic"`) for MECH-168 / INV-047's staged-decline
  prediction, with the non-vacuous gain readout MECH-169's falsifier requires.
- Reusable per-phase functional-integrity instrumentation for any future
  consolidation-pipeline experiment.

## Prerequisite caveat -- MECH-121 hold (respected, not lifted)

MECH-121 is `candidate/substrate_conditional` (`hold_pending_v3_substrate/applied`).
The hold suppresses surfacing MECH-121 for **promotion** work. This harness is
representation-level plumbing instrumentation on injected content, **not** MECH-121
behavioural validation. Any run built on it:

- MUST be `EXPERIMENT_PURPOSE="diagnostic"`;
- MUST NOT tag MECH-121 as promotion evidence or change its status;
- treats the NREM leg as a substrate-plumbing-fidelity readout only.

The staging diagnostic is a property of the pipeline WIRING (error-propagation
topology), measurable regardless of MECH-121's behavioural-validation status.

## Related Claims

MECH-120, MECH-121 (held), MECH-123, MECH-168 (staged failure), INV-047 (staged
clinical decline), MECH-169 (glymphatic/attribution complementarity -- V3-testable
staging content folded onto INV-047/MECH-168 via /claim-synthesis), MECH-204, SD-017.
