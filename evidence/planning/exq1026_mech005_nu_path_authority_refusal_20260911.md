# V3-EXQ-1026 (MECH-005 nu path-authority live agent) -- REFUSED, not queued

**Session:** queue-stranded-1018-1003-20260911, 2026-09-11T23:49:00Z.
**Chip:** chip-20260910-recover-stranded-exq-1018-1003.
**Authorisation:** user approved the recovery attempt 2026-09-10 ("Recover both via
/queue-experiment", recommendation-agreement ledger entry 201) and the launch 2026-09-11
(entry 238). The refusal is this session's finding, not a user instruction.
**Disposition:** NOT QUEUED. The driver stays UNTRACKED at
`ree-v3/experiments/v3_exq_1018_mech005_nu_path_authority_live_agent.py` with a
DO-NOT-QUEUE banner, mirroring the precedent set for V3-EXQ-1003 on 2026-09-09.
Reserved id **V3-EXQ-1026 is released** (the file's own `1018` was already burned --
see "ID collision" below).

## What this driver was for

MECH-005 ("Path authority and interruptibility via norepinephrine-like control") has
ZERO experimental manifests -- 0 of 1013 packs tag it, which proposal EVB-1381 flags as
`missing_experimental_evidence + synthetic_signals_only`. The only adjacent evidence,
V3-EXQ-505, injected a SYNTHETIC z_beta into a bare MultiRateClock and so verified the
interpolation arithmetic of `clock.update_e3_rate_from_beta` and nothing downstream.

This driver was the live-agent counterpart: endogenous z_beta, real candidates, real E3
selection, asking whether raising arousal converts a deliberation-RATE change into a
change in PATH AUTHORITY per deliberation opportunity. That is a real and unoccupied
question, and the intent behind this driver remains worth pursuing. What follows is
about the instrument, not the question.

## The design was substantially careful

Stated so the refusal is not read as a verdict on the author's work. The driver already
got right nearly everything the `/queue-experiment` checklist asks for: `alpha_world=0.9`
(SD-008), `zworld_p0_episodes=8` (SD-070), seed 44 excluded for early-death instability,
per-arm precondition gates via `_lib/precondition_gate` rather than a whole-run AND (the
V3-EXQ-785 defect), the E3 `last_*` latch cleared before every select with `n_latched`
recorded (the V3-EXQ-785 ~9x pseudo-replication defect), cells stamped reuse-INELIGIBLE
with a truthful reason, a DV chosen upstream of `torch.multinomial` for cross-machine-class
portability, an explicit per-arm DV-symmetry declaration, and the urgency factor
demoted out of C1 after the smoke showed the DV arithmetically invariant to it.

The three gates this session ran before the red-team all passed:

* **Step 2.5b re-derive brake:** 0 counted autopsies on MECH-005. Not braked.
* **V3-pending gate:** MECH-005 is `status: provisional` with no `v3_pending` and no
  `implementation_phase`. Not held.
* **Step 2.5c substrate-path overlap:** four open `corrupting` entries exist, and the one
  that looked like a hit is not one. Details below, because the measurement is reusable.

## Step 2.5c: measured, not argued (reusable finding)

Three of the four open `corrupting` entries hold **no instance** in this driver's
configuration -- `MECH-320` (`policy/tonic_vigor.py`), `sd_blocked_agency_mismatch_floor_calibration`
(`affect/blocked_agency.py`) and `sd105_frozen_shared_entropy_floor_multiplier`
(`regulators/selection_entropy_floor.py`). Their modules are eagerly imported by
`ree_core`, so an import-level test reads as an overlap; an attribute scan of the built
agent plus instrumented `__init__` counters over a full dry-run recorded zero
instantiations of any of them.

The fourth, `contextmemory-write-path-addressing-degeneracy`
(`predictors/e1_deep.py::ContextMemory.write`, severity `corrupting`, status
`implemented_pending_validation` = still OPEN), does sit on a class the agent HOLDS
(`agent.e1.context_memory`). It is nonetheless **structurally unreachable here**:

* `ContextMemory.write` has exactly ONE call site, `E1DeepPredictor.update_from_observation`
  (`e1_deep.py:1272`).
* That is reached only from `agent.py:10957`, gated on
  `E1Config.sd016_writepath_mode in ("train_only", "both")`.
* The default is `"off"` (confirmed on this driver's own constructed config), and the
  driver never sets it.
* Measured over a complete dry-run (training + all four measurement arms):
  `ContextMemory.write` **0 calls**, `ContextMemory.read` **332 calls**. The defect's own
  title states the READ path already has the non-degenerate selection the WRITE path lacks.

So the gate is clear on a function-granular, measured basis rather than by assertion.

## ID collision (independent of the refusal)

The file is named `v3_exq_1018_*` and the chip recorded the slot as "reserved but never
written". **V3-EXQ-1018 is in fact BURNED**: `experiments/v3_exq_1018_mech222_self_attribution_contamination.py`
is tracked on `origin/main`, and commit `5cd2882` closed that id ("mark MECH-222 driver
NOT QUEUED -- EXP-0893 -> blocked_substrate"). Any successor to this driver needs a fresh
number, not `1018`. This session reserved and then released `V3-EXQ-1026`.

## The refusal: what the red-team found, and what was verified at source

Step 4.5 red-team, reviewer model **fable**, single pass, foreground. **VERDICT: BLOCKING.**
Each load-bearing finding below was re-verified against the source by this session before
being accepted -- a reviewer finding is a lead, not a verdict.

### F1 (BLOCKING) -- the environment is never stepped during measurement

`_measure` calls `env.reset()` once (driver line 379) and **never steps the environment**:
`grep -c "env.step"` over the whole driver returns **0**, and `obs_dict` is assigned
exactly twice in the file (line 342 in `_build`, line 379 in `_measure`) and never
reassigned. The measurement loop (lines 409-523) therefore calls
`agent.sense(obs_dict["body_state"], obs_dict["world_state"], ...)` on **one frozen
observation** for all `MEASURE_TICKS=900` ticks of every arm, and the action returned by
`select_action` is never applied to anything.

This falsifies the design's own central premise. The docstring states (lines 141-154)
that "raising the E3 rate changes WHEN selection happens, so the high-arousal arm samples
a DIFFERENT distribution of world states" and names that as the run's one inherent,
measured-not-asserted confound. There is no distribution: there is a single state.

What the arousal contrast then reduces to, per the reviewer's measurements on the
driver's own `_measure` path (seeds 42/43, 540 ticks): the observation was unchanged
300/300 ticks in every arm; the RNG state at the k-th fresh select was identical at
`beta_magnitude_scale` 0.1, 1.0 and 10; and the k-th margin was *exactly* equal between
LO and HI for 22/30 and 20/28 values of k. Because the two arousal arms differ only in
how MANY fresh selections they draw from one fixed per-seed sequence (~45 in LO vs ~180
in HI at 900 ticks), the recorded HI-LO delta is the difference between the mean of the
first ~45 and the first ~180 draws of the same sequence. Truncating HI to LO's draw count
collapsed the driver's deltas from -0.00296/+0.01862 to -0.00036/-0.00131.

**Unattributable under every outcome.** A C1 PASS records
`nu_modulates_path_authority_per_opportunity` (or `..._inverse`) with
`evidence_direction: "supports"` on what is a sample-count artifact; a C1 FAIL records
`nu_modulates_deliberation_rate_only` with `evidence_direction: "weakens"` against
MECH-005 on an instrument that never varied the quantity the claim is about. Neither can
be attributed to nu. The reviewer additionally computed the C1 gate's pass rate under a
pure null at **10.5%** (analytic, t(2) >= 2.828 given `np.std` ddof=0 over 3 seeds plus
sign consistency), so roughly one run in ten of this artifact would have recorded
experimental support for a claim that currently has none at all.

### F2 (confirmed) -- the covariate-overlap gate certifies its own subject

`arousal_arm_state_covariate_overlap` (ceiling 0.25) exists solely to guard the confound
F1 dissolves. It is computed from `hazard_prox_mean`, which is accumulated at driver line
505 from `obs_dict["hazard_field_view"]` -- the frozen observation. Both arms therefore
read the same constant and the measured gap is ~2e-16. **The gate cannot fail.** Note the
docstring records an earlier `max()` -> `mean()` fix here (because `max()` saturated at
1.000 and "would have made the check trivially met and certified nothing"); that fix
treated a symptom of this same frozen observation.

### F3 (confirmed) -- two diagnostic keys are never written, and one gate passes on the absence

`e3_score_decomp_enabled` defaults to **False** (`e3_selector.py:614`) and the driver
**never sets it** (0 occurrences; the cited instrument V3-EXQ-785a sets it twice). The
E3 diagnostics dict consequently never carries `urgency_applied`, `committed` or
`commit_variance`. Two consequences:

* `fidelity_errs` stays empty, so `urgency_fidelity_max_err` is `nan`, and driver line 698
  coerces a non-finite value to **0.0**, which passes the `upper`-bound ceiling of 1e-6.
  The urgency-fidelity readiness precondition is **vacuously met** -- it certifies an
  instrument that was never read. The docstring's citation of 785a's 2.8e-17 fidelity does
  not transfer, because 785a enabled the flag that produces the number.
* `n_committed` is 0 in every arm, so `commit_channel_live` (floor 10) is red every run by
  instrumentation rather than by substrate. The commitment-pressure diagnostic is
  correctly walled off from C1 and so vacates nothing, but it cannot report either.

### Lower-severity, recorded for a successor

* **F5** `clock.py:211-221` clamps `t = min(1, max(0, ||z_beta|| * scale))`, so at
  `scale=10` any `||z_beta|| >= 0.1` pins `e3_steps` at 5 and at `scale=0.1` it sits at
  18-19. Measured: one `e3_steps` value per arm on every tick while `||z_beta||` took
  22-23 distinct values. The arm labelled "ENDOGENOUS z_beta" is, at these two scales,
  operating a saturated clamp -- the endogenous variation is clamped out.
* **F6** DV scale was seed-heterogeneous by ~10x under dry-run training (seed 42 ~0.025 vs
  seed 43 ~0.28). Because C1 compares absolute per-seed deltas, one seed can set the SD
  term. May compress under full training; unverified.
* **C1_ABS_FLOOR is binding, not an anti-degeneracy guard.** The docstring asserts
  "C1_ABS_FLOOR (1e-3) is only an anti-degeneracy guard ...; the SD term is the binding
  gate". Since `c1_required = max(C1_ABS_FLOOR, 2*SD)`, whichever is LARGER binds, and in
  a low-between-seed-variance regime the uncalibrated absolute floor binds. This session
  confirmed it by driving the analysis with stubbed cells: a delta of **0.0012** with tiny
  between-seed SD returns C1 PASS -> `supports`, against a measured DV of only ~0.013-0.026.

### Verified NOT findings

`arm_cell`'s RNG reset (`arm_fingerprint.py:808-811,845`) and
`capture/restore_agent_surface` (`probe_warmup.py:367-431`) behave as documented; the
urgency cells are bit-identical within an arousal level exactly as the docstring predicts;
`fresh_selects_per_cell` (~45 measured at 900 ticks vs floor 30) and
`e3_rate_separation` are both attainable. The `assert_no_structurally_unsatisfiable_gate`
call at line 605 is inert because no structural bounds are declared on the specs.

## Why this is a refusal rather than a fix

F1 is not a narrow repair. Stepping the environment changes the state distribution the DV
is measured over, which changes the DV's scale and variance, which invalidates every
pre-registered threshold in the script (all of them were calibrated against the frozen-
observation smoke, including the C1 floor, `MIN_FRESH_SELECTS`, and
`COVARIATE_OVERLAP_MAX`), and it re-arms the inherent state-sampling confound that F2's
gate was supposed to measure but cannot. It also changes what the run costs. That is a
redesign requiring its own smoke, its own bar derivation and its own red-team -- i.e. a
fresh `/queue-experiment` pass on a new EXQ number, not an edit to this file.

Per the chip's own instruction, a refusal with a recorded reason is the correct outcome
here, and is better than queueing ~18 minutes x 3 seeds of fleet compute that could only
produce an unattributable manifest against a claim with zero existing evidence.

## What a valid successor would need

1. **Step the environment during measurement**, with the executed action applied, so
   there is a state distribution for arousal to shift.
2. **Then re-derive every threshold** from a fresh smoke on the stepped design -- none of
   the current constants survive.
3. **Enable `e3_score_decomp_enabled`** (as V3-EXQ-785a does) so `urgency_applied`,
   `committed` and `commit_variance` are actually written; and make the urgency-fidelity
   precondition treat a non-finite measurement as UNMET rather than coercing it to 0.0.
4. **Re-point the covariate-overlap gate** at a quantity that can differ between arms once
   the env is stepped, and confirm it can fail.
5. **Calibrate C1's absolute floor to the measured DV scale**, or drop it and let the SD
   term bind alone as the docstring intends; and record `np.std`'s `ddof` choice explicitly.
6. **Address the `e3_steps` clamp saturation (F5)** -- pick arousal levels that do not pin
   the interpolation at both ends, or the "endogenous z_beta" framing is not earned.
7. Consider whether a per-opportunity authority DV can be read at all while the E3 rate is
   the manipulated variable, since the number of opportunities is itself the manipulation.

## Reproduction

```
# F1, the whole finding in one line:
grep -c "env.step" ree-v3/experiments/v3_exq_1018_mech005_nu_path_authority_live_agent.py   # -> 0
grep -n  "obs_dict *=" ree-v3/experiments/v3_exq_1018_mech005_nu_path_authority_live_agent.py  # -> 342, 379 only

# F3:
grep -n "e3_score_decomp_enabled" ree-v3/ree_core/predictors/e3_selector.py | head -1   # :614 = False
grep -c "e3_score_decomp" ree-v3/experiments/v3_exq_1018_mech005_nu_path_authority_live_agent.py  # -> 0

# Step 2.5c write-path unreachability:
grep -n "context_memory.write" ree-v3/ree_core/predictors/e1_deep.py        # single site :1272
grep -n "update_from_observation" ree-v3/ree_core/agent.py                  # :10957, sd016_writepath_mode gated
```

Red-team findings artifact (reviewer model fable, session scratchpad, not version
controlled): `redteam_1026_findings.md`, with probes `rt1026_probe_frozen_obs.py`,
`rt1026_probe_tickphase.py`, `rt1026_probe_align.py`, `rt1026_c1_null.py`.
