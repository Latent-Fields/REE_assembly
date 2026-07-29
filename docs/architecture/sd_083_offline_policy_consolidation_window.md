---
status: candidate_substrate_landed
status_asof: 2026-07-29
status_claim: SD-083
---

# SD-083: sleep.offline_policy_consolidation_window

**Claim ID:** SD-083
**Subject:** consolidation.offline_policy_window (trace-selective, interval-accumulated, novelty-gated)
**Registered:** 2026-07-29
**Depends on:** MECH-475 (mech457_policy_kl_anchor -- the sibling ONLINE anchor this reuses the snapshot pattern from), MECH-441 (RND novelty drive -- PRINCIPLE reused; the lineage's own RNDModule is the instantiation), the mech457 bootstrap-explorer testbed (RepAgent / train_bootstrap_explorer / train_a2c)
**Blocks:** MECH-476 INTERVAL arm (V3-EXQ-836b) and NOVELTY arm (V3-EXQ-836c) -- the two `blocked_substrate` legs of the MECH-476 three-arm retrograde-interference falsifier

## Problem

MECH-476 (`competence_retention_dissociable_from_acquisition`, candidate / v3_pending)
asserts that consolidation is properly defined as RESISTANCE TO RETROGRADE INTERFERENCE
(Krakauer, Ghez & Ghilardi 2005), and therefore should depend on install DOSE and on
elapsed offline INTERVAL -- and, per its distinctive content (iii), should be TRACE-SELECTIVE
(synapse-specific), which a global coefficient cannot express.

The DOSE axis is buildable on the existing substrate and was queued as V3-EXQ-836. The other
two axes are not, because **REE has no offline window in which a consolidation process acts on
a POLICY**:

- The `ree_core/sleep/` cluster (SleepLoopManager, SleepReplaySampler, the SWS/REM passes,
  MECH-272/273/275/285, the MEL consumer) consolidates the **REEAgent's E1/E2/E3 latents,
  world-model and self-model** -- never an actor policy. (Verified 2026-07-29: zero
  `policy`/`actor`/`a2c` references in `ree_core/sleep/*.py` outside MEL duration-scaling.)
- The MECH-457/476 retention lineage runs a **separate testbed stack** -- a minimal
  actor-critic `RepAgent` trained by `experiments/_lib/mech457_bootstrap_explorer`. Its only
  offline compute is credit-replay *inside* the RL refinement. The one policy-protection
  mechanism it has, `PolicyKLAnchor` (MECH-475), is **online / undifferentiated**: a global
  logit-space KL to a frozen snapshot, constructed at RL entry, with no elapsed interval and
  no per-parameter selectivity.

This is exactly the **Walker 2003 divergence** the MECH-476 literature review records: REE's
protection is awake, online, and undifferentiated, whereas biological consolidation is
sleep-dependent, offline, and trace-selective. Without an offline, trace-selective,
novelty-gated window, MECH-476's INTERVAL and NOVELTY predictions cannot be tested at all.

## Solution

A new **offline policy-consolidation window** inserted into the bootstrap-explorer testbed
BETWEEN `install_bc_prior` (policy installed, `post_bc` measured) and `train_off_arm` (the
interfering unconstrained RL refinement). It is built in `experiments/_lib/`, alongside its
sibling `PolicyKLAnchor` -- the same locus MECH-475 landed in, NOT `ree_core/`. It is a
**falsifier instrument**, not a cognifold faculty (see "Architecture Context" for the
registered port-to-cognifold follow-on).

**The window builds protection; it does NOT retrain.** During the window the installed policy
parameters theta are left UNCHANGED, so `post_bc` competence is invariant to the interval.
This is the property that makes the INTERVAL axis orthogonal to the DOSE axis: dose moves
theta* itself (a stronger install), whereas the interval only builds the trace-selective
protection erected AROUND a fixed theta*. Biological consolidation is protection of a trace,
not re-acquisition of it.

New module `experiments/_lib/mech457_offline_consolidation.py`:

1. **`OfflineEWCAnchor(theta_star, fisher_diag, coef)`** -- a trust-region anchor whose penalty
   is the **parameter-space, Fisher-weighted (EWC; Kirkpatrick et al. 2017) sum**
   `coef * sum_i F_i * (theta_i - theta*_i)^2`, added once per episode update in `train_a2c`.
   Because the Fisher diagonal is estimated from the gradient of the policy log-likelihood
   `log pi(a|s)`, value-head-only parameters receive ~0 Fisher and are therefore left
   unconstrained -- the same locus discipline as `PolicyKLAnchor` (the shared trunk moves on
   both; the value estimator locus stays with MECH-459). Trace selectivity is expressed by
   `F_i`: only parameters important to the installed competence are protected.

2. **`consolidate_offline_window(rep, demo, ..., offline_window_steps, novelty_pairing, ...)`**
   -> `OfflineEWCAnchor` or `None`. During the window:
   - Snapshot `theta* = frozen copy of the installed policy` (reuses the `PolicyKLAnchor`
     deepcopy pattern).
   - Estimate the **Fisher diagonal** by offline replay of the demonstrator's on-expert states
     (SWS-analog): at each replayed state, sample `a ~ pi(.|s)`, backprop `log pi(a|s)`,
     accumulate `grad^2` over `offline_fisher_samples` state-action pairs. No env reward, no RL,
     no optimiser step on theta.
   - Accumulate a **capture resource** `c(N) = capture_max * (1 - exp(-N / tau))`, `N =
     offline_window_steps` (Moncada 2007 tag-and-capture / Bin-Ibrahim 2024 synaptic-tagging
     systems-consolidation clock). This is the interval-dependence: `N = 0 -> c = 0 -> no
     anchor is returned -> unconstrained control`.
   - **Novelty gating** (Moncada 2007 behavioural tagging), `novelty_pairing`:
     - `"none"` -- capture proceeds at full strength (`novelty_factor = 1.0`). Used by the
       INTERVAL arm, where novelty is not the manipulation.
     - `"paired"` -- a novelty exposure runs inside the window; the lineage's own `RNDModule`
       (RepAgent feature space) measures mean predictor-error over it, and
       `novelty_factor = clamp(novelty_score / novelty_ref, tag_leak, 1.0)`.
     - `"unpaired"` -- no novelty exposure (or a familiar one); `novelty_factor = tag_leak`
       (a small floor -- the weak tag is not captured and decays).
   - Effective coefficient `coef = offline_ewc_max_coef * c(N) * novelty_factor`.

`train_a2c` gains one optional keyword `offline_ewc_anchor` (default `None`) and one penalty
term at the existing update site; `train_bootstrap_explorer` threads it. Both no-op when the
window is disabled.

**Config** (added to `BootstrapExplorerConfig` in `mech457_bootstrap_explorer.py` -- this
lineage has its OWN config object; it does NOT use `ree_core/utils/config.py::REEConfig`). All
defaults no-op:

| Param | Type | Default | Purpose |
|-------|------|---------|---------|
| `use_offline_consolidation` | bool | False | master switch |
| `offline_window_steps` | int | 0 | interval N (Fisher passes + capture clock) |
| `offline_capture_tau` | float | 200.0 | capture time-constant |
| `offline_capture_max` | float | 1.0 | capture ceiling |
| `offline_ewc_max_coef` | float | 0.0 | max EWC coefficient (scaled by capture x novelty) |
| `offline_fisher_samples` | int | 256 | state-action pairs for the Fisher estimate |
| `offline_novelty_pairing` | str | "none" | none / paired / unpaired |

## Architecture Context

**Not a duplicate of the landed MECH-475 KL anchor -- this IS the scientific content.**

| | MECH-475 `PolicyKLAnchor` | SD-083 offline window |
|---|---|---|
| When | ONLINE (during RL) | OFFLINE (a real A->B interval before RL) |
| Selectivity | global (logit-space KL, all params equal) | TRACE-SELECTIVE (Fisher per-parameter) |
| Interval dependence | none (constructed at RL entry) | capture `c(N)` accumulates over N |
| Novelty gating | none | Moncada behavioural tagging |

SD-083 lets MECH-476 test the distinctive content MECH-475 structurally cannot: (ii) an offline
interval, and (iii) trace selectivity.

**Testbed-first, with a registered cognifold port (user decision 2026-07-29).** REE is one
cognifold; this build is deliberately in the falsifier testbed, not the cognifold, following
the same probe-gated discipline (and the same `experiments/_lib/` locus) as the landed MECH-475
anchor. The measurement is kept clean by isolating it from the cognifold's other faculties. IF
MECH-476's arms come back SUPPORTED, the cognifold-level consequence -- registered as a
follow-on, not pre-built -- is to port offline, trace-selective, **novelty-gated** consolidation
of the policy/action pathway into the ONE SD-017 sleep loop, unifying with MECH-441 novelty and
MECH-204. MECH-476's own cross-link already names `sleep_substrate_plan.md` SD-017/MECH-204 as
that eventual home.

## What This SD Enables

- **V3-EXQ-836b (INTERVAL):** vary `offline_window_steps` at fixed install dose. SUPPORTED
  (for MECH-476) if `retained_fraction` grows monotonically with the interval.
- **V3-EXQ-836c (NOVELTY):** a weak-but-took ("sub-threshold") install x {paired, unpaired}
  novelty in the window at fixed interval. SUPPORTED if the weak install is retained only in
  the novelty-paired condition (behavioural tagging).
- The SD-083 validation experiment (diagnostic): ON-vs-OFF ablation proving the window
  populates a non-trivial Fisher-weighted anchor, that its coefficient scales with N and with
  novelty, and that it measurably raises retained_fraction vs the unconstrained control.

## MECH-094 and phased training

- **MECH-094: N/A.** The window computes policy-parameter statistics (theta*, Fisher, capture)
  from the demonstrator's REAL on-expert trajectories. Nothing simulated is written to any
  memory store, so the hypothesis-tag requirement does not apply.
- **Phased training: N/A.** raw_view has no encoder head to warm up; the reference build runs
  the encoder detached; the window acts on the already-installed policy and takes no optimiser
  step on theta. There is no moving-target head-collapse hazard.

## Related Claims

MECH-476 (parent), MECH-475 (sibling online anchor), MECH-457/459/460 (retention lineage),
MECH-441 (novelty principle), SD-017 / MECH-204 (cognifold sleep home for the eventual port).
