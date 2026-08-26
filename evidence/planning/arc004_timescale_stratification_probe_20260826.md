# ARC-004 probe: is L-space actually stratified by TIMESCALE?

**Date:** 2026-08-26 · **Session:** `insights-7fd98a` · **Status:** FINDING -- read-only measurement, nothing registered, no claim status changed.
**What this is:** the first execution of **ARC-004's own registered `what_would_answer`**, which
states the claim "has never been tested as its own claim (absent from `claim_evidence.v1.json`)
-- it is currently assumed via **36 dependents' architecture**, not measured."
**Probes:** `arc004_halflife_probe.py` + follow-ups (session scratch, read-only; no repo writes).

---

## Verdict: **FAIL** on ARC-004's own criteria -- "layers differ in content, not timescale"

ARC-004's PASS branch requires a monotonic ordering of persistence,
`half-life(z_delta) > half-life(z_theta) > half-life(z_beta)`, by a margin exceeding
**0.8 SD of the seed-to-seed delta**. Measured at three operating points, 5 seeds each
(distinct stack init AND distinct input stream per seed), 1500 ticks, warmup discarded:

| operating point | seeds with predicted ordering | mean(delta - beta) | 0.8 x SD bar | verdict |
|---|---|---|---|---|
| synthetic AR(1) rho=0.5 | **1/5** | +0.043 | 0.060 | FAIL |
| synthetic AR(1) rho=0.95 | **1/5** | +0.041 | 0.653 | FAIL |
| **real `CausalGridWorld` rollout** | **0/5** | **-0.159** | 0.142 | **FAIL** |

On the real environment the margin is not merely below the bar -- it points the **wrong
way**: z_delta's half-life is *shorter* than z_beta's on every seed.

Per-layer means on the real rollout: beta 6.187, theta 5.890, delta 6.028 -- a spread of
~5% of the mean, with no monotone ordering.

## Why, and the mechanism is transparent

Two facts, both read from source:

1. **One shared, hardcoded clock.** `ree_core/latent/stack.py:1454`:
   `alpha_shared = 0.3  # z_beta/theta/delta use a shared alpha`, applied identically:
   ```python
   z_beta  = alpha_shared*z_beta  + (1-alpha_shared)*prev_state.z_beta
   z_theta = alpha_shared*z_theta + (1-alpha_shared)*prev_state.z_theta
   z_delta = alpha_shared*z_delta + (1-alpha_shared)*prev_state.z_delta
   ```
   Note `alpha_self` and `alpha_world` ARE configurable (`getattr(self.config, ...)`);
   `alpha_shared` is a **bare local literal** with no config path at all. ARC-004's own
   non-degeneracy precondition already records this and correctly says the claim is therefore
   *not* vacuously true -- differentiation would have to emerge from the cascade instead.
2. **The cascade cannot supply it, because the cascade is static.** `combined -> beta -> theta
   -> delta` (`stack.py:1345-1347`) with top-down `delta -> theta -> beta`, but every stage is
   an **untrained** projection (MECH-523: the three encoders appear ZERO times in `agent.py`,
   no loss, no optimiser). A static map changes *values*, not *temporal correlation*. So each
   depth inherits its input's timescale and is filtered by one identical EMA.

The white-noise control confirms it exactly: at rho=0 all three measure 1.89-1.91 against the
EMA-alone prediction of `ln(0.5)/ln(0.7) = 1.94`. The EMA is the only temporal filter present,
and it is the same one three times.

## What follows

ARC-004's FAIL branch states the consequence itself: *"This would not remove the layers'
functional roles but would mean 'multi-timescale' is the wrong description of why they work,
structurally analogous to what happened to MECH-058, and would prompt a supersession review of
ARC-004's framing."*

The MECH-058 precedent its own text cites is exact: MECH-058 asserted timescale separation for
the z_self/z_world split, was tested in V3-EXQ-019 by lag-k autocorrelation, FAILED, and was
retired -- superseded by MECH-069 ("incommensurable domains", not timescale). The same
substitution looks available here: the layers plainly differ in *content* and *role*; what is
unsupported is that they differ in *rate*.

**Status: ARC-004 is `active`, `epistemic_category: standard`, with 36 dependents.** No status
change is made here -- that is `/governance`'s call. Raised as a governance flag.

## Honest limits -- read before acting on this

- **Untrained encoders.** This is the as-built condition (MECH-523), and ARC-004's own
  precondition frames the test that way, so it is the right condition for the claim *as posed*.
  A trained stack is untested, and if the depth encoders ever acquire a training signal the
  measurement must be repeated.
- **Random-action policy.** The real-environment rollout uses real observation statistics but a
  random policy. A trained agent's trajectory could carry different temporal structure.
- **Observation routing is approximate.** The 210-dim env observation was split in half into
  `body_obs_dim` / `world_obs_dim` for stack construction; the real harness routes specific
  channels. This should be redone with the canonical routing before any supersession decision.
- **The optional corroboration was not run.** ARC-004's `what_would_answer` also invites a
  per-layer decomposition of MECH-423's `inference_convergence` readout (currently a single
  relative-delta over the concatenated vector). Not done here.
- Three operating points, 5 seeds each. Consistent, but this is one session's measurement.

## Why this was worth running at all

ARC-004's falsifier was already written, fully specified, with a PASS/FAIL margin rule and a
named precedent -- and had never been executed. That is the **third** instance this session of
the same pattern: MECH-464 and MECH-465 likewise sat with written falsifiers, literature on
file, and no run (five weeks); MECH-518's registered check would have auto-refuted itself. The
common factor is not difficulty -- this probe is ~40 lines and needs no substrate change -- it
is that nothing routes a written falsifier to anyone. See GFLAG-0054 for the mechanical half of
that (zero-evidence claims never enter the backlog `/lit-pull` and the proposal queue read).
