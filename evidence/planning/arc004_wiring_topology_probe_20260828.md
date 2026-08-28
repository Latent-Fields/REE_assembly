# ARC-004 is vacuously FALSE by construction: the depth cascade has no cross-tick path

**Date:** 2026-08-28 · **Session:** `elated-nobel-914234` (continuation of `insights-7fd98a`)
**Status:** FINDING -- source inspection + derivational toy. Read-only measurement. Nothing registered, no claim status changed, no substrate change.
**Probe:** [`arc004_wiring_topology_probe_20260828.py`](arc004_wiring_topology_probe_20260828.py) (numpy, no torch, no substrate import).
**Predecessor:** [`arc004_timescale_stratification_probe_20260826.md`](arc004_timescale_stratification_probe_20260826.md) (GFLAG-0055) measured the FAIL. This asks *why*, and the answer changes the disposition.

---

## Verdict

The ARC-004 null is a **WIRING** absence, not a **TRAINING** absence. The
distinction is not academic: it inverts the remedy, and it means the
2026-08-26 FAIL is not evidence against timescale stratification as an
architectural principle.

Three findings, in order of how much they change what governance should do:

1. **ARC-004's own non-degeneracy precondition asserts something that is false
   in source, and has been false since ree-v3's first commit.**
2. **The consequence is that the claim was vacuously FALSE by construction** --
   its falsifier could only ever return FAIL. The precondition was written to
   rule out vacuous *truth* and did not consider the other direction.
3. **A serial-smoothing wiring reaches ARC-004's PASS criterion with UNTRAINED
   encoders**, so supplying a training signal to the as-built wiring would not
   have helped, and the training-absence reading (MECH-523) does not explain
   this null.

---

## 1. The precondition is false in source

ARC-004's `what_would_answer` states:

> "any timescale differentiation must emerge from the recursive top-down
> architecture (z_delta reads only z_theta's **history**, z_theta reads only
> z_beta's, so information at each level is progressively more temporally
> aggregated) rather than from a built-in rate split."

That is the sentence doing all the work: it is what licenses treating a null as
"possible and must be measurable, not assumed away". It is wrong.

`ree_core/latent/stack.py`:

- **l.1326-1327** -- `combined_init` is built from `split_encoder(body_obs, world_obs)`
  on the **current** observation only. No previous state enters it.
- **l.1345-1347** -- the cascade is entirely within-tick:
  ```python
  z_beta_init, _  = self.beta_encoder(combined_init)
  z_theta_init, _ = self.theta_encoder(z_beta_init)     # z_beta_init, not history
  z_delta, _      = self.delta_encoder(z_theta_init)    # z_theta_init, not history
  ```
- **l.1349-1353** -- the top-down round (`delta_to_theta`, `theta_to_beta`) also
  operates on within-tick values.
- **l.1373-1400** -- the optional MECH-423 settling loop explicitly holds the
  bottom-up data terms fixed and runs *before* the EMA, so it too adds no
  cross-tick structure.
- **l.1508-1510** -- `prev_state.z_beta`, `prev_state.z_theta` and
  `prev_state.z_delta` occur at **exactly these three lines in the entire file**
  (verified by grep), as a terminal EMA applied **in parallel** with one shared
  constant:
  ```python
  alpha_shared = 0.3  # bare literal; alpha_self / alpha_world ARE configurable
  z_beta  = alpha_shared * z_beta  + (1 - alpha_shared) * prev_state.z_beta
  z_theta = alpha_shared * z_theta + (1 - alpha_shared) * prev_state.z_theta
  z_delta = alpha_shared * z_delta + (1 - alpha_shared) * prev_state.z_delta
  ```

So the depth stack is **three parallel first-order low-pass filters with
identical time constants**, applied to three different *instantaneous* functions
of the same input. There is no cascade of filters and no progressive temporal
aggregation anywhere in the path.

**This is not drift.** `git log -S "prev_state.z_delta"` and
`git log -S "self.theta_encoder(z_beta_init)"` both return a single commit:
`3c264ac`, "Initial ree-v3 substrate build". The stack has never been serial.
The class docstring's "Shared stack: (z_self + z_world) -> z_beta -> z_theta ->
z_delta" reads as a temporal cascade and is a within-tick function composition.

## 2. Therefore the claim was vacuously FALSE, and the falsifier could only FAIL

The precondition's purpose was to establish that ARC-004 is "NOT vacuously true
by construction". It succeeds at that and misses the mirror case. With a shared
parallel filter and a within-tick cascade, differential persistence has no
mechanism to arise from -- so the claim is vacuously **false** by construction,
and its registered falsifier is not a test but a foregone conclusion.

That is why the disposition matters. A FAIL from a test that could have passed
is evidence about the architecture. A FAIL from a test that could not have
passed is evidence about the implementation. GFLAG-0055 currently reads the
2026-08-26 result the first way, citing the MECH-058 precedent. MECH-058 is
**not** the right precedent: MECH-058's z_self/z_world split was tested in
V3-EXQ-019 on a substrate where `alpha_self` and `alpha_world` are genuinely
separate configurable constants, so its falsifier could have passed and did not.
ARC-004's could not.

## 3. The toy: serial wiring passes, UNTRAINED

Four arms, sharing an input stream and random encoders per seed. Encoders match
`SharedDepthEncoder`: `Linear(in,64) -> ReLU -> Linear(64,out)`, scaled by
`sigmoid(0) = 0.5`, no training. Scored on ARC-004's own criterion -- monotone
half-life ordering `delta > theta > beta` by a margin exceeding `0.8 * SD` of
the seed-to-seed `(delta - beta)` delta.

| arm | wiring | beta | theta | delta | d-b | 0.8*SD | mono | verdict |
|---|---|---|---|---|---|---|---|---|
| A | as-built (within-tick cascade, parallel EMA) | 13.43 | 12.27 | 11.30 | **-2.136** | 0.415 | 0/5 | **FAIL** |
| B | serial cascade over the SMOOTHED value, ReLU | 13.43 | 13.90 | 14.14 | +0.704 | 0.362 | 4/5 | **PASS** |
| C | serial cascade, LINEAR encoders | 15.78 | 17.44 | 18.69 | +2.914 | 0.386 | 5/5 | **PASS** |
| D | as-built wiring, per-layer alphas 0.5/0.3/0.1 | 11.78 | 12.27 | 18.43 | +6.646 | 0.331 | 5/5 | **PASS** |

(AR(1) rho=0.95, 5 seeds, T=4000, alpha=0.3.)

Robustness across input autocorrelation, 8 seeds:

| rho | A (as-built) | B (serial, ReLU) | C (serial, linear) |
|---|---|---|---|
| 0.00 | -0.008  2/8 FAIL | +4.241  8/8 PASS | +4.467  8/8 PASS |
| 0.50 | -0.210  0/8 FAIL | +3.370  8/8 PASS | +3.596  8/8 PASS |
| 0.90 | -1.078  0/8 FAIL | +2.057  8/8 PASS | +3.101  8/8 PASS |
| 0.95 | -2.212  0/8 FAIL | +0.873  7/8 PASS | +3.074  8/8 PASS |
| 0.99 | -10.757 0/8 FAIL | -8.012  0/8 FAIL | +0.166  0/8 FAIL |

Three things fall out.

**(a) Arm A independently reproduces the 2026-08-26 white-noise control from
pure topology.** At rho=0 it gives 1.96 / 1.95 / 1.95 against that probe's
measured 1.89-1.91 and the EMA-alone analytic value `ln(0.5)/ln(0.7) = 1.94`.
One filter, three times -- derived here rather than inferred.

**(b) Arm A's inversion has a mechanism.** Each successive untrained ReLU
projection destroys some of the input's autocorrelation, so the deeper layer's
*instantaneous* signal is less persistent, while the shared EMA adds the same
fixed amount to each. Depth therefore makes persistence **shorter**, and
increasingly so as the input becomes more autocorrelated. **SUPERSEDED BY S8:**
this section originally read that the inversion "explains the sign the
predecessor probe measured on the real environment (-0.159, 0/5 seeds) and left
unexplained". The real-stack follow-up in S8 shows the real stack does NOT
invert, so the toy's inversion is an artefact of its own missing top-down and
precision machinery and explains nothing about the predecessor's number. The
arm-A/arm-B contrast is unaffected; only this attempted explanation is withdrawn.

**(c) Training is neither necessary nor sufficient.** Arm B passes with random
untrained encoders; arm A fails with them and would still fail with trained
ones, because training changes the instantaneous map `f` and not the filter
topology. Three parallel identical EMAs remain three parallel identical EMAs
however well `f` is trained.

## 4. What this does and does not say about MECH-523

MECH-523's methodological corollary is that a null measured at an untrained
compression site is evidence about the absence of a training signal, not about
capacity. Site (b) of MECH-523 is exactly this depth stack, so the corollary
appears to apply -- and on this evidence **it does not**, because the missing
ingredient here is wiring rather than training.

The corollary is not wrong; it is **too narrow**. The general form is: *a null
measured at a site whose mechanism is absent is evidence about the absent
mechanism.* "Untrained" is one species of absent mechanism. "Unwired" is
another, and this case is the second. That widening is offered for governance,
not made here. Note the direction: MECH-523's own notes anticipate governance
possibly *narrowing* the claim to site (b) at n=3; this argues the corollary
should widen on a different axis while the site enumeration stands unchanged.

## 5. What it pulls into V3 -- the actual dependency question

**(a) One new V3 substrate item, which did not previously exist.** To make
ARC-004 testable at all, the depth stack needs a cross-tick path. Two candidates:

- **Serial smoothing (arm B)** -- feed the *smoothed* `z_beta` into
  `theta_encoder`, and the smoothed `z_theta` into `delta_encoder`. This is the
  wiring ARC-004's precondition already describes in words, so it is arguably a
  correction rather than an addition. Produces the ordering *emergently*, which
  is what the precondition demanded.
- **Per-layer alphas (arm D)** -- `alpha_beta` / `alpha_theta` / `alpha_delta`
  via `getattr(self.config, ...)`, exactly mirroring `alpha_self` / `alpha_world`
  three lines above (SD-008). Trivial, but ARC-004 explicitly calls a built-in
  rate split vacuous-by-construction, so this satisfies the claim in the way the
  claim says is uninteresting.

Both are small and both have precedent in the same function; the flag-gated,
bit-identical-when-OFF pattern is already established there by
`use_iterative_inference`. **Arm B is the one that matches the claim's own
stated architecture.** This is `complicated (buildable)`, not
`complex (probe-gated)` -- the probe has already been run.

**(b) It does NOT pull in 36 dependents.** ARC-004 has 38 claims naming it in
`depends_on`. Scanning their text for rate/timescale vocabulary returns 13, and
of those only four are load-bearing on *rate* rather than on layered *content*:
MECH-001, MECH-058 (already retired for this exact reason), MECH-520 and
MECH-523. The remaining ~34 depend on ARC-004 for the existence and
differentiated content of a layered stack -- which ARC-004's own FAIL branch
explicitly preserves ("would not remove the layers' functional roles"). The
"36 dependents" figure is the claim's *citation* count, not the blast radius of
this result, and the two should not be conflated in a supersession review.

**(c) MECH-520 does not move to v3 on this evidence.** The prior reading in this
thread was that a minimal MECH-520 predictive-obligation head was the V3 pull,
on the argument that untrained encoders were the blocker. Arm B refutes it: the
ordering appears untrained once the wiring is serial. MECH-520 keeps its `v4`
phase; its own content (anti-collapse constraint on a value-carved
representation) is untouched by this.

## 6. Honest limits -- read before acting

- **The toy is not the stack.** numpy, random encoders, AR(1) input, no
  top-down loop, no precision gating, no split encoder, no reafference
  correction. It models the *temporal topology* and nothing else. Its claim is
  about what the topology can and cannot produce, not about V3's behaviour.
- **It disagrees with the predecessor probe on the sign of a sub-bar effect.**
  At synthetic AR(1) rho=0.5 the 2026-08-26 probe measured +0.043 (1/5 seeds,
  below its 0.060 bar); this toy measures -0.210 (0/8, above its 0.033 bar). The
  two agree on the white-noise control and on the real-environment sign, and
  agree that no monotone ordering emerges. The disagreement suggests the real
  stack's top-down and precision machinery partially offsets the per-stage
  decorrelation -- worth checking on the real stack before quoting the toy's
  inversion magnitude for anything.
- **Arm B is regime-dependent.** It fails at rho=0.99, where per-stage
  decorrelation outruns the cascade gain. The real environment's measured
  half-lives (~6) put it near rho~0.9, where arm B passes 8/8 -- but this should
  be confirmed on the real stack, not assumed from the toy.
- **Arm B is a proposal, not a specification.** ARC-004 describes it in prose;
  no REE claim specifies it. Whether the divergence means the claim's
  description is wrong or the implementation is, is a governance/user call and
  is deliberately not made here.
- **No status change and no substrate change is made here**, per the standing
  rule that dispositions route through `governance_flag.py`.

## 7. The pattern this makes four of

The predecessor probe closed by noting that MECH-464 and MECH-465 sat five weeks
with written falsifiers unrun, MECH-518's registered check would have
auto-refuted itself, and ARC-004's falsifier was fully specified and never
executed -- with GFLAG-0054 naming the mechanical half (nothing routes a written
falsifier to anyone).

This adds a fourth and slightly different instance: ARC-004's falsifier was not
merely unrun, it was **unrunnable as a test** -- its precondition made a
checkable factual assertion about the substrate that nothing checked, and that
had been false since the substrate's first commit. The gap is not only "nobody
runs the falsifiers" but "nobody checks that a falsifier's stated preconditions
hold in source before the claim is treated as tested-in-principle". That is a
cheaper check than running the falsifier, and it is the one that would have
caught this.

---

## 8. REAL-STACK FOLLOW-UP (same session) -- the toy's central claim holds, its explanation of the predecessor's sign does not

Everything above is a numpy topology toy, and S6 flagged "the toy is not the
stack" as its first limit. That limit is now closed by running both arms on the
**real `LatentStack`** with **canonical observation routing**, and the result
both confirms the main finding and forces one withdrawal.

**Probe:** [`arc004_realstack_probe_20260828.py`](arc004_realstack_probe_20260828.py).
Both arms are built by calling the stack's own submodules -- real
`SharedDepthEncoder`s, real `delta_to_theta` / `theta_to_beta` top-down maps,
real precision gating, real `SplitEncoder` -- so they differ **only** in where
the EMA sits. No substrate file is modified.

**Fidelity, checked before anything was measured:**
`max |arm-A manual - real stack.encode()| = 0.000e+00` over 40 ticks. Arm A is a
bit-identical reimplementation of the shared-stack path, so the comparison is
against the real thing rather than a model of it.

**Canonical routing, and why the predecessor's was not.** `CausalGridWorld`
declares `body_obs_dim = 10`, `world_obs_dim = 200`, and the flat observation
tensor is verified equal to `cat(body_state, world_state)` -- so
`_split_observation`'s `observation[:, :body_obs_dim]` is canonical at 10/200.
The 2026-08-26 probe used `REEConfig.from_dims(body_obs_dim=OBS//2, ...)`, i.e.
105/105, giving `z_self` 105 channels instead of 10.

**Result, 10 seeds, T=1500, random policy:**

| arm | beta | theta | delta | d-b | 0.8*SD | mono | verdict |
|---|---|---|---|---|---|---|---|
| A -- as-built | 5.00 | 5.05 | 5.10 | +0.102 | 0.354 | 4/10 | **FAIL** |
| B -- serial smoothing | 5.00 | 7.71 | 9.34 | **+4.342** | 0.510 | **10/10** | **PASS** |

**The headline survives, and is now measured rather than modelled: serial
smoothing reaches ARC-004's own PASS criterion, on the real stack, with
untrained encoders, at a margin 8.5x its bar and 10/10 seeds.**

### 8.1 The correction: the FAIL is robust, the "wrong direction" is not

Arm A was re-run across eight method variants -- routing (10/200 vs 105/105) x
half-life estimator (this session's standardised form vs the predecessor's
full-series-variance form) x action count (4 vs 5; `action_dim` is 5) x env
seeding (seeded vs unseeded) -- 10 seeds each:

| n_act | env seeded | routing | d-b | bar | mono |
|---|---|---|---|---|---|
| 4 | yes | canonical | +0.034 | 0.562 | 3/10 |
| 4 | yes | half-split | +0.050 | 0.330 | 3/10 |
| 4 | no | canonical | +0.036 | 0.521 | 4/10 |
| 4 | no | half-split | +0.021 | 0.358 | 2/10 |
| 5 | yes | canonical | +0.102 | 0.354 | 4/10 |
| 5 | yes | half-split | +0.079 | 0.448 | 3/10 |
| 5 | no | canonical | +0.073 | 0.340 | 2/10 |
| 5 | no | half-split | -0.037 | 0.355 | 2/10 |

Every variant is far below its own bar; monotone-ordering count is 2-4 of 10
throughout; and the **sign flips** with choices that carry no theoretical
weight. The two estimators agree to three decimals on identical trajectories
(+0.102 vs +0.099 canonical, +0.079 vs +0.079 half-split), and
`REEConfig.from_dims(...).latent` was checked field-by-field against a plain
`LatentStackConfig` and is **identical**, so neither is the source of the
difference.

So the honest characterisation of the as-built stack is **"no ordering; the
effect is indistinguishable from zero and its sign is unstable"** -- not "the
margin points the wrong way".

**The predecessor's script is also not deterministic.** Recovered from the
originating session's transcript, it constructs `CausalGridWorld()` with **no
seed** while seeding only torch and numpy, so the environment varies run to run.
Re-running it as recovered gives `-0.125` and `-0.097` on successive runs
against its reported `-0.159` -- same band, not reproducible to the digit.

**What this changes, and what it does not.** ARC-004's FAIL verdict is
*strengthened*: it now reproduces across routing, estimator, action count, env
seeding and seed count, and at 10 seeds rather than 5. What does not survive is
the rhetorically stronger reading -- "z_delta persists SHORTER than z_beta on
every seed", which reads as active evidence against timescale stratification.
It is a 5-seed reading of a zero-centred noise band. Anyone quoting the
2026-08-26 result in a supersession review should quote the FAIL and not the
direction.

### 8.2 Withdrawal

S3(b) above originally offered the toy's arm-A inversion as the explanation of
that -0.159. Since the real stack does not invert, there is nothing to explain,
and the toy's inversion is an artefact of the machinery the toy omits (top-down
maps and precision gating, both of which the real stack has and the toy does
not). That paragraph is marked superseded in place. The toy's arm-A/arm-B
*contrast* is unaffected and is confirmed by the real-stack run above.

### 8.3 What is still open

- **Arm B is measured untrained and unfree.** A serial stack that is also
  trained is untested, and MECH-520's predictive obligation would land exactly
  there. Nothing here says what serial + trained does.
- **Random policy.** Both arms use it. A trained agent's trajectory statistics
  could differ.
- **Arm B changes downstream behaviour.** Every consumer of z_beta / z_theta /
  z_delta sees different values. Nothing here measures that, and it is the
  reason any build must be flag-gated and bit-identical when OFF.
- **The toy's rho=0.99 failure was not re-tested in vivo.** The real
  environment's measured half-lives (~5) sit well inside the band where arm B
  passes, so this is not currently load-bearing.
