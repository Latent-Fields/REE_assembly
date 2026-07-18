---
status: candidate
status_asof: 2026-07-18
status_claim: SD-068
---

# SD-068: sleep.consolidation_pipeline_lesion_harness

**Claim ID:** SD-068
**Subject:** sleep.consolidation_pipeline_lesion_harness
**Registered:** 2026-07-17
**Depends on:** SD-017 (offline SWS/REM passes), MECH-120 (SWS denoising), MECH-121 (NREM slot-filling, *held*), MECH-123 (REM precision recalibration), MECH-204 (precision-recalibration consumer)
**Blocks:** the MECH-168 / INV-047 / MECH-169 staged-decline falsifier; a representation-level staged-damage diagnostic (V3-EXQ-778 + power-up V3-EXQ-778a, run 2026-07-17; generative-gain non-vacuity banked offline -- see **Diagnostic results**)

> **SCOPE NARROWED 2026-07-18 (V3-EXQ-778c null control), THEN PARTIALLY RE-WIDENED
> 2026-07-18 (V3-EXQ-778g).** The 778c null control retired the ORIGINAL `sws` readout
> (`sws_denoising_snr`, content-free by construction, `null_slope_ratio` 1.0000 on 8/8
> seeds) and found `rem` degenerate at both clamp rails, leaving `nrem` as the only
> confirmed content-contingent leg. The routed repair then landed and was validated:
> `_sws_pattern_completion` (ree-v3 `main` `8b18338`) clears the SAME load-bearing C1
> criterion at the SAME 0.25 ceiling that admitted `nrem` --
> `null_slope_ratio_sws` mean **0.1495** (sd 0.0218, CI95 [0.1344, 0.1646]),
> `ceiling_inside_ci95` FALSE, **8/8 seeds** (V3-EXQ-778g, run_id
> `v3_exq_sd068_sws_content_scored_readout_diagnostic_20260718T130139Z_v3`, ree-cloud-2,
> PASS) -- so the `sws` leg is **RE-ADMITTED** to the non-vacuity contract.
>
> **Live contract:** SD-068's non-vacuity is carried by **TWO** confirmed
> content-contingent per-phase readouts -- `nrem` injected-content AND the rebuilt `sws`
> pattern-completion -- plus the REM passthrough-vs-generative contrast.
>
> **Still excluded:** the reverse-dependency **STAGING ORDER** remains UNSUPPORTED, and
> the staging-order results in **Diagnostic results** stay RETRACTED as staging evidence.
> 778g gates on `gated_phase` `sws` ALONE (nrem/rem measured as context only); staging is
> a CROSS-phase ranking and cannot be supported while the `rem` leg has no interpretable
> readout, and no run has re-measured the order with the repaired instrument. The
> **NARROW-SUPPORTS FLAG stays raised** on narrower ground: the REM generative-gain
> pillar's own content-dependence is open (`H-gen-gain-content-free`, owned by the
> GOV-FANOUT-1 portfolio V3-EXQ-778d/e/f, all still queued as of 2026-07-18). Both 778c
> and 778g are DIAGNOSTIC: no status, confidence, promotion or demotion change; SD-068
> remains `candidate` / `implementation_phase v3` and the MECH-121 hold stands.
> See **Null-content control (V3-EXQ-778c)** and **SWS readout rebuild**. Authoritative
> live scope: the SD-068 `evidence_quality_note` in `docs/claims/claims.yaml`.

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
  **>> RETIRED AS A CONTENT READOUT 2026-07-18 (V3-EXQ-778c null control).** This
  statistic is **content-free**: `noise_power` is identical with and without injected
  content at every `sigma`, so the sigma-slope is driven entirely by `log(noise_power)`
  and the content term differentiates away. Measured `null_slope_ratio` = 1.0000
  (sd 2.7e-8) on 8/8 seeds. It has never measured content fidelity and must not be
  scored as damage tolerance until replaced by a content-scored readout (the same
  repair as `rem_terrain_variance` -> `rem_generative_fidelity`). Retained as telemetry
  only. See **Null-content control** below.
  **>> REBUILT 2026-07-18 (ree-v3 `main` `8b18338`); see "SWS readout rebuild" below.**
- `_sws_pattern_completion` -- **the content-scored replacement for the scored sws
  series (2026-07-18).** Cosine retrieval margin of the post-SHY store against the
  injected prototypes: `margin_i = cos(probe_i, shy(store)_i) - max_{j != i}
  cos(probe_i, shy(store)_j)`. Probed with the UNSCALED prototypes, so the null arm
  gets a real, arm-identical probe that is simply not planted. **VALIDATED 2026-07-18
  by V3-EXQ-778g** (8 seeds, PASS): `null_slope_ratio_sws` mean 0.1495 (sd 0.0218,
  CI95 [0.1344, 0.1646]), `ceiling_inside_ci95` FALSE, 8/8 seeds, against the same
  0.25 ceiling that admitted `nrem`. This is the SCORED `sws` series.
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

- **`nrem` fails before `sws` -- ~~ROBUST~~ RETRACTED as evidence of staging
  (2026-07-18, V3-EXQ-778c).** The measurement stands -- `sws_tolerance -
  nrem_tolerance` > 0 on **8/8** seeds (mean +0.424, 95% CI [0.422, 0.425], sign-test
  p = 0.0078) -- but its *interpretation* does not. The null control shows the `sws`
  pole of this adjacency is a **content-free** readout (`null_slope_ratio` 1.0000 on
  8/8 seeds), so this compares a content-contingent readout (`nrem`) against a noise
  statistic (`sws`). It is not evidence that failure is staged. *The `sws` pole here is
  the RETIRED `sws_denoising_snr` readout; the 2026-07-18 rebuild + 778g validation does
  NOT reinstate these numbers, because `tolerance_sigma_sws` flows through the replaced
  series and the order has not been re-measured. This retraction STANDS.*
  **The tell was already in this table:** `sws` tolerance std ~9e-9 against `nrem`
  0.0014 and `rem` 0.396, and a 95% CI of width 0.003. That tightness was read as
  robustness; it is the signature of a near-deterministic analytic metric. *A per-phase
  variance three-to-five orders of magnitude below its siblings is an instrument-validity
  flag, not a strength-of-effect signal.* See **Null-content control** below.
- **`rem` fails first -- CONTESTED / seed-variable.** `nrem_tolerance -
  rem_tolerance` mean -0.097, 95% CI [-0.43, +0.23] straddles 0 (4/8 seeds positive,
  sign-test p = 1.0). The REM-first leg is underpowered at n=8; `rem` tolerance is
  the high-variance phase (std 0.396 vs `nrem` 0.0014, `sws` ~9e-9).
- Overall Spearman mean rho = 0.375 (95% CI [-0.25, +1.00], includes 0); Kendall's
  W = 0.328 (Friedman chi2 = 5.25, df 2). Modal observed order `(rem, nrem, sws)` on
  4/8 seeds.

~~So the *reverse-dependency staging* is **partially supported**: the NREM-before-SWS
adjacency is robust; the REM-fails-first adjacency is not resolved at this power.~~
**SUPERSEDED 2026-07-18.** After the null control, the honest reading is: the
NREM-before-SWS adjacency is *uninterpretable* as staging (content-free `sws` pole),
and the REM-fails-first adjacency remains unresolved at this power. **No leg's staging
POSITION has been established.** *(Wording corrected 2026-07-18 after V3-EXQ-778g: this
originally read "no leg ... is currently supported by a validated instrument", which is
now false as written -- two of the three legs, `nrem` and the rebuilt `sws`, have
validated content-contingent instruments; the third, `rem`, does not. The staging
conclusion is unchanged.)*
All three phases do degrade monotonically with `sigma` (load-bearing C1 PASS, corr
>= 0.96 each) and are non-degenerate at `sigma = 0` (P0 control) -- but monotone
degradation with `sigma` is exactly what a noise-sensitivity statistic also produces,
so it does not discriminate.

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

> **OPEN QUESTION on the "intact seed" gloss (flagged 2026-07-18, V3-EXQ-778c).** In
> the null control's manifest the **null arm's** `rem_generative_gain` (seed 42:
> 0.182 / 0.184 / 0.188 / 0.209 across `sigma`) is close to the injected arm's
> (0.165 / 0.166 / 0.172 / 0.190) at `rem_gen_content_scale` 0.0. This sits OUTSIDE
> the scored C1 criteria and is recorded as an open question, **not** a verdict. If it
> replicates it does not touch the attenuation finding itself -- the transfer function
> does attenuate -- but it would undercut the specific gloss that the correction
> *needs an intact seed*, since attenuation would then occur with no seed content at
> all. Registered as hypothesis `H-gen-gain-content-free` in
> `hypothesis_space_registry.v1.json`; probe sketched in
> `failure_autopsy_V3-EXQ-778c_2026-07-18`.

(`rem_passthrough_calibration_slope` -- the raw `calibration_error`-vs-`sigma` slope
in variance units -- ranges 0.03-599 across seeds; it is scale-variable telemetry
under the `step=1.0` full-adoption measurement choice, NOT the dimensionless gain, and
is NOT load-bearing. The by-construction passthrough *gain* is 1.0; the load-bearing
contrast is generative-gain 0.149 << 1.)

### Null-content control (V3-EXQ-778c, 2026-07-18) -- the instrument-validity audit

> **Reading note (added 2026-07-18).** Everything in this subsection is TRUE OF THE
> INSTRUMENTS AS THEY STOOD ON 2026-07-18 MORNING, and is retained as history. Its `sws`
> findings pertain to the **RETIRED `sws_denoising_snr` readout**, which was subsequently
> replaced and re-validated -- see **SWS readout rebuild** below. V3-EXQ-778c is **NOT
> superseded**: it is what motivated and justified the repair, and 778g audits a
> different instrument. Its `rem` finding is still live.

**This is the load-bearing correction to everything above.** The zero-injected-content
null control (the analog of the odour-contingency null in Bar et al. 2020, the
methodological precedent this SD follows) ran the identical `sigma` sweep twice per
seed on identical substrate / warm-up / RNG streams, differing only in
`content_scale` (1.0 vs 0.0), with the delivered perturbation held numerically
identical across arms via `diffuse_perturb(rms_ref=...)`. 8 seeds (the 778a set).
Reported per phase as `null_slope_ratio` = |null sigma-slope| / |injected sigma-slope|
-- ~0.0 means content-contingent, ~1.0 means fully confounded.

`v3_exq_sd068_null_content_control_diagnostic_20260718T072318Z_v3`, ree-worker-1,
**FAIL / weakens**. Load-bearing C1 failed on **0/8 seeds**. Readiness precondition met
(injected slope 0.0665 >> 1e-06 floor) and C2 passed, so this is an informative negative
about the instrument, **not** a broken run.

| phase | mean `null_slope_ratio` | sd | 95% CI | seeds confounded | verdict |
|-------|------------------------|-----|--------|------------------|---------|
| `nrem` | **0.1445** | 0.00090 | [0.1438, 0.1451] | 0/8 | **content-contingent** -- the one working leg |
| `sws` (RETIRED `sws_denoising_snr`) | **1.0000** | 2.7e-08 | [0.99999997, 1.00000001] | 8/8 | **fully confounded -- content-free** *(instrument since replaced; the rebuilt `_sws_pattern_completion` scores 0.1495 -- see 778g below)* |
| `rem`  | 1911.6 | 3306.1 | [-379, 4203] | 3/8 | **degenerate / uninterpretable** |

- **`sws` (the RETIRED `sws_denoising_snr`) is content-free by construction.** At every `sigma` the injected arm has
  `signal_power` 5585.7 and the null arm 0.0, while `noise_power` is *identical* in
  both (384.18 / 1536.73 / 6146.91 / 24587.64). Since
  `denoising_snr_db = 10*log10(signal_power / noise_power)`, the sigma-slope depends
  only on `log(noise_power)`; the content term is a constant offset that differentiates
  away. This is analytic, not statistical -- hence sd 2.7e-8.
- **`rem` is degenerate at both rails.** Exactly `0.0` on 5/8 seeds (the null arm's
  `calibration_error` pins at the constant 998.5009992509989 with `target_clamped` 1.0,
  so the slope is identically zero) and off-scale 1801-9143 on 3/8 (the null precision
  reference collapses onto the 1e-3 positivity floor, so `1/1e-3` dominates).
  `ceiling_inside_ci95` is true and `confound_verdict_stable` false. The 5
  apparently-clean seeds are clean only *by degeneracy*.

**Consequence for SD-068 (claim NARROWED, not withdrawn).** Per this experiment's own
pre-registration ("a FAIL here is an INFORMATIVE outcome... it scopes SD-068's
non-vacuity honestly rather than withdrawing the claim"), the non-vacuity contract is
now carried by the `nrem` injected-content leg and the REM passthrough-vs-generative
contrast **only** -- not by the `sws` leg. Note this leaves SD-068 resting on a single
confirmed content-contingent readout plus a generative-gain contrast whose own
content-dependence is itself an open question (see the OPEN QUESTION box above): do not
read the narrowing as leaving SD-068 comfortably supported.

> **PARTIALLY RE-WIDENED 2026-07-18 (V3-EXQ-778g).** The exclusion of the `sws` leg rested
> on one stated ground and one only -- its readout was content-free by construction -- and
> that ground is now discharged by the rebuilt, validated `_sws_pattern_completion` (see
> **SWS readout rebuild**). The contract is henceforth carried by **TWO** confirmed
> content-contingent readouts (`nrem` + rebuilt `sws`) plus the REM contrast. The
> NARROW-SUPPORTS caution above is **NOT** cleared, only narrowed: the generative-gain
> pillar's content-dependence is still open (`H-gen-gain-content-free`), and the staging
> order is still unsupported. Do not read the re-widening as leaving SD-068 comfortably
> supported either; it restores one readout to the contract, nothing more.

**Routing:** `/implement-substrate` to replace `sws_denoising_snr` with a content-scored
readout (experiment-layer, `_lib/consolidation_lesion_harness.py`, zero `ree_core`
change) + a GOV-FANOUT-1 three-axis portfolio on the `rem` leg. Full diagnosis:
`evidence/planning/failure_autopsy_V3-EXQ-778c_2026-07-18.{md,json}`.

### SWS readout rebuild (2026-07-18, ree-v3 `main` `8b18338`) -- BUILT AND VALIDATED (V3-EXQ-778g)

The routed repair has landed and has since been validated at 8 seeds (see **Validation**
at the end of this subsection). `denoising_snr_db` is retained as telemetry; the SCORED
sws series is now `_sws_pattern_completion`.

**The design move.** Any readout of the form `f(shy(damaged) - shy(clean))` is
content-free for an affine `shy` -- that is the whole defect, and it is analytic, not
statistical. The replacement therefore scores a RELATIONAL IDENTITY rather than a
residual energy: after damage and denoising, can each injected prototype still be
IDENTIFIED in the store? The score is a ratio of correct-vs-incorrect cosine similarity
whose denominators carry `clean`, so the affine cancellation no longer removes the
content term. This is the same escape `rem_generative_fidelity` made from
`rem_terrain_variance`: route the readout through an operation the content genuinely
survives in, and score against the KNOWN injection.

**The load-bearing detail -- probe with the UNSCALED prototypes.** Probing with `clean`
(`= base * content_scale`) would make the null arm's probe the zero vector and the
readout 0/0-degenerate. A zero from an undefined similarity is exactly the `rem` leg's
existing failure mode, where 5/8 "unconfounded" seeds are unconfounded only BY
DEGENERACY. Probing with `base` instead delivers a real, non-degenerate, arm-identical
probe that is simply not planted in the null arm -- the direct analog of Bar et al.
2020's "same odour delivered, no prior pairing".

**Local smoke (seeds 42/7/123) -- NOT evidence at seed scale:**

| seed | injected slope | null slope | `null_slope_ratio_sws` | contingent |
|------|----------------|------------|------------------------|------------|
| 42 | 0.3246 | 0.0376 | 0.116 | yes |
| 7 | 0.3434 | 0.0586 | 0.171 | yes |
| 123 | 0.3578 | 0.0544 | 0.152 | yes |

`confounded_phases` is now `['rem']` alone. Note the ratios VARY across seeds, unlike
the retired readout's 1.0000 (sd 2.7e-8) -- per this doc's own instrument-validity
lesson, seed-to-seed scatter is what a measurement looks like and near-zero variance is
what an analytic identity looks like.

**Declared caveat on that pass.** The readout is cosine-based and therefore
SCALE-INVARIANT, and `phase_integrity_at_sigma` reseeds per sigma, so in the null arm
(store = `0 + sigma*noise`) the sigma factor cancels out of the cosine entirely. The
null arm is flat in sigma PARTLY BY CONSTRUCTION, which makes the null control a weaker
independent check for this readout family than the ratio alone suggests. A
content-scale ladder (`content_scale` in {0.0, 0.25, 0.5, 1.0}) was run as the
independent check: sigma-slope is exactly 0.0 at zero content and 0.449 / 0.430 / 0.325
above it. The slope DECREASES as content strengthens because damage is referenced to
`_rms(base)` (the unscaled prototypes) and so is held at full strength regardless of
content amplitude -- weakly planted content faces proportionally larger damage and is
destroyed faster. That is content-tracking in the physically correct direction.

**Validation -- V3-EXQ-778g (2026-07-18, PASS/supports, DIAGNOSTIC).** Three local seeds
were not evidence -- the 778c autopsy's own lesson is that low-n reads hide unstable
verdicts -- so the null control was re-run on the repaired readout at the full 8-seed
778a set, carrying the content-scale ladder as a second criterion. Run
`v3_exq_sd068_sws_content_scored_readout_diagnostic_20260718T130139Z_v3`, ree-cloud-2:

| criterion | result | verdict |
|-----------|--------|---------|
| C1 `null_slope_ratio_sws` vs the 0.25 ceiling | mean **0.1495**, sd 0.0218, CI95 [0.1344, 0.1646], `ceiling_inside_ci95` **FALSE**, **8/8 seeds** | PASS -- content-contingent |
| C3 content-scale ladder (slope spread vs 0.01 floor) | spread **0.1108** | PASS -- discharges the cosine scale-invariance caveat |

C1 is the SAME criterion at the SAME ceiling that admitted the `nrem` leg -- re-admitting
`sws` on a weaker test than the one that excluded it would be motivated reasoning. C3
matters because the replacement is cosine-based and hence scale-invariant, so its null
arm is flat in sigma partly BY CONSTRUCTION (the caveat declared above); the ladder means
the result does not rest on the null ratio alone.

**So the `sws` leg IS a validated instrument as of 778g, and is re-admitted to the
non-vacuity contract.** The staging order nonetheless **remains unsupported**: 778g gates
on `gated_phase` `sws` ALONE, with `nrem` and `rem` measured and reported as CONTEXT ONLY
and deliberately not gated (the `rem` leg is degenerate at both clamp rails, so gating all
three would FAIL regardless of whether the `sws` repair worked). What 778g validates is
the `sws` INSTRUMENT's content-contingency, not any staging result -- staging is a
CROSS-phase ranking, and no run has yet re-measured it with the repaired instrument.

V3-EXQ-778c is **not** superseded by this: its finding is about the RETIRED readout and
is what motivated the repair; 778g validates a DIFFERENT instrument.

**Consequence for prior runs.** V3-EXQ-778 / 778a drivers still RUN (the SNR keys are
still emitted), but their staging numbers are NOT reproducible across this change,
because `tolerance_sigma_sws` flows through the repaired series. That is intentional --
those numbers were retracted as staging evidence above.

(V3-EXQ-778b, `...20260718T065939Z_v3`, is the n=2 predecessor of this control and is
marked `superseded`: same conclusion, strictly dominated evidence, rem leg unresolved
at n=2.)

### Combined diagnostic reading

**REVISED 2026-07-18 after the null control.** The 2026-07-17 reading was: staging
order **partially confirmed** (NREM-before-SWS robust; REM-first
seed-variable/underpowered), with the vacuity threat refuted by a strongly attenuating
REM generative gain. The null control revises the first half and leaves the second
standing:

- **Staging order: NOT currently supported.** The NREM-before-SWS adjacency as measured
  is uninterpretable (its `sws` pole was the content-free retired readout) and the
  REM-first adjacency was already contested and underpowered. *Updated 2026-07-18 after
  V3-EXQ-778g:* two of the three per-phase readouts (`nrem` and the rebuilt `sws`) are
  now confirmed to measure content, but the `rem` leg remains degenerate and no run has
  re-measured the order with the repaired instrument -- so no leg's staging POSITION is
  established. Staging is a cross-phase ranking and cannot be supported while one ranked
  leg has no interpretable readout.
- **Non-vacuity (REM generative gain 0.149, 8/8 attenuating): STANDS.** It is a
  different readout (`rem_generative_fidelity`) with its own internal
  clean-vs-corrupt control, and C1 does not bear on it. The narrower "correction needs
  an intact seed" gloss is flagged as an open question.

So the honest combined reading is: **the pipeline has a real error-propagation transfer
function (REM generative gain) and two validated content-contingent per-phase
instruments (`nrem`, rebuilt `sws`), but the evidence that its failure is STAGED remains
unsubstantiated -- limited now by the uninterpretable `rem` leg and by the absence of any
re-measurement with the repaired instrument.** This remains DIAGNOSTIC --
it promotes and demotes nothing, MECH-121 stays held (NREM leg plumbing-fidelity only),
and per-claim `evidence_direction` on MECH-168 / INV-047 / MECH-169 is `unknown`
(they are context tags; the control audits the instrument, not the claims).

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
