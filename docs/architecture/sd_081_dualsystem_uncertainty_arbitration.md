# SD-081: e3.dualsystem_uncertainty_arbitration

**Claim ID:** SD-081
**Subject:** e3.dualsystem_uncertainty_arbitration
**Status:** IMPLEMENTED
**Registered:** 2026-07-22
**Implemented:** 2026-07-22
**Depends on:** ARC-007, ARC-016, SD-005, MECH-112
**Blocks:** MECH-477 (falsifier), MECH-163 leg (1) retest

## Problem

MECH-163 asserts that two goal-directed systems run in parallel -- a habit system
(SNc/dorsal-striatum, model-free, cached S-R) and a hippocampally-planned system
(VTA/ventral-striatum + PFC, model-based, multi-step rollout) -- and that the planned
system is preferentially recruited in novel contexts.

V3-EXQ-786a tested that proposition and returned a flat response: recruitment delta
mean 0.00435, Cohen's d 0.047, 7 of 8 seeds within +/-0.15, on a run whose manipulation
check passed with real headroom (familiarity discriminability AUC 0.848 against a 0.7
bar, n=8, `non_degenerate: true`).

The `failure_autopsy_V3-EXQ-786a_2026-07-22` diagnosis: **differential recruitment is
not a property of having two systems, it is the output of an ARBITRATOR that reads
uncertainty and reallocates control.** MECH-477 (registered 2026-07-22) names that
element. The substrate had two pathways and no arbitrator, and the code says so
plainly -- `E3Selector.select()` scored candidates with an unconditional full-horizon
`J(zeta)`, with no weight anywhere between the myopic and the deep read. There was
nothing that *could* respond to novelty.

### A second, independent defect found while building this (see "Finding" below)

V3-EXQ-786a's recruitment DV was **itself degenerate**, for a reason unrelated to the
arbitrator. This is recorded here because it bears directly on how the SD-081 falsifier
must be designed, and it is adjudication work owed to `/failure-autopsy` and
`/governance` -- **not settled by this document.**

## Solution

An explicit arbitration weight over the two pathways' contributions to E3 selection,
driven by their relative predictive uncertainty.

### The two pathways

Inherited from V3-EXQ-786a's operationalisation, deliberately -- the falsifier is a
two-arm OFF-vs-ON contrast of that design, so the pathways must be the same objects:

| Pathway | Read |
|---|---|
| **Habit** (model-free) | `score_trajectory` depth-limited to `dualsystem_habit_depth` (default 2) |
| **Planned** (model-based) | `score_trajectory` at full horizon -- the pre-SD-081 selection score |

Depth-limiting is applied inside `E3Selector._get_world_states()`, through which every
`compute_*` cost component reads its states. One truncation therefore makes all of
F / M / Phi_R / B / goal myopic together: the habit pathway is a depth-limited read of
**the same machinery**, not a second scorer that could drift from the planned one.

### The arbitration weight

```
u_habit    = 1 - familiarity(z_world)        [novel context -> HIGH]   (fallback: E1 novelty EMA)
u_planned  = E3._running_variance            [bad forward model -> HIGH]

u_n        = u / (u + ema_of_u)              per pathway; 0.5 at its own baseline

w_planned  = sigmoid( gain * (u_habit_n - u_planned_n) + bias )
```

Daw, Niv & Dayan 2005 (Nature Neuroscience 8(12):1704-1711, conf 0.79, on file at
`evidence/literature/targeted_review_connectome_mech_163/2026-04-05_mech163_uncertainty_competition_daw2005`):
control is allocated to whichever controller is **less uncertain**. Novel context ->
`u_habit` up -> `w_planned` up -> deep rollout dominates selection. Practised context ->
the reverse.

The per-pathway EMA normalisation is load-bearing, not tidiness. Familiarity is a
clamped proximity-weighted kernel density whose scale is set by `familiarity_bandwidth`;
`_running_variance` is an unbounded PE-MSE. A ratio taken over the raw values would be
an artifact of the instrument rather than a reading of the two pathways -- the same
defect V3-EXQ-786a fixed when it replaced a raw mean-difference manipulation check with
an AUC.

### The blend

```
z_h = zscore(J_habit) ;  z_p = zscore(J_planned)
scores = mean(J_planned) + std(J_planned) * ( (1-w) * z_h + w * z_p )
```

Three reasons the standardisation is required rather than cosmetic:

1. `J_habit` sums over 2 steps and `J_planned` over `horizon+1`, so blending the raw
   costs would make `w` a **gain** on the planned pathway rather than an **allocation**
   between two.
2. Standardisation is rank-preserving, so neither pathway's own candidate ordering is
   distorted by the rescale.
3. At `w = 1` the blend returns the planned vector exactly, so the ON arm is a readable
   departure from the OFF arm rather than a different experiment.

### Where it lands

Immediately after the per-candidate score stack in `E3Selector.select()` and **before**
`raw_scores`. Everything downstream -- `raw_score_range`, the `score_bias` channels, the
commit gate, the argmin and the softmax -- therefore sees the arbitrated score. That
makes the arbitration a genuine reallocation of control, which is what MECH-477 asserts.
Blending after the bias channels would instead arbitrate a score those channels had
already shaped.

### Config (E3Config)

| Param | Default | Purpose |
|---|---|---|
| `use_dualsystem_arbitration` | `False` | master switch |
| `dualsystem_arbitration_gain` | `4.0` | sigmoid slope on relative uncertainty |
| `dualsystem_arbitration_bias` | `0.0` | operating-point shift |
| `dualsystem_uncertainty_ema_alpha` | `0.05` | per-pathway uncertainty baseline |
| `dualsystem_habit_depth` | `2` | depth of the habit read (floored at 2, see Finding) |

**These live on `E3Config`, not `REEConfig`.** `E3Selector.config` IS the `E3Config`, so a
REEConfig-level field reads as a missing attribute in the selector and defaults to
`False` -- the silently-unreachable-flag hazard one level below the documented
`from_dims` one. This build tripped exactly that during authoring (arbitrator wired,
kwargs arriving, 45 `select()` calls, zero arbitrations) and both levels are now pinned
by `tests/contracts/test_sd081_dualsystem_arbitration.py`.

### Instrumentation

`E3Selector.last_arbitration` carries the paired series per E3 tick:
`w_planned`, `u_habit_raw`, `u_planned_raw`, `u_habit_norm`, `u_planned_norm`,
`u_habit_ema`, `u_planned_ema`, `habit_uncertainty_source`, `habit_score_range`,
`planned_score_range`, `degenerate`, `degeneracy_reason`.

MECH-477 makes it **mandatory** that the falsifier show the arbitration weight varies
with measured uncertainty -- otherwise a null is a readiness failure scoring nothing
rather than a refutation. This dict is what that check consumes. `None` when the
arbitrator is off; only meaningful on an E3 tick (between ticks the held action is
returned and the field retains its previous value).

## Finding: V3-EXQ-786a's recruitment DV was degenerate

**Confirmed by measurement under 786a's own config, not inferred.**

786a computed `recruitment = 1 - spearman(full_horizon_scores, first_step_scores)` with
the first-step read taken as `evaluate_trajectory(world_seq[:, :1, :])`.

Index 0 of the z_world sequence is the **current** state -- shared by every candidate,
since they all start from where the agent actually is. Measured on a 32-candidate set
under `build_config` + `ArmSpec(arm_id="mech163_recruitment")`, on 786a's own
`_depth_scores`:

```
tick 1 | n=32 | FIRST-STEP range=0  n_unique=1 | FULL range=0.0496
tick 2 | n=32 | FIRST-STEP range=0  n_unique=1 | FULL range=0.0668
tick 3 | n=32 | FIRST-STEP range=0  n_unique=1 | FULL range=0.0733
tick 4 | n=32 | FIRST-STEP range=0  n_unique=1 | FULL range=0.0607
tick 5 | n=32 | FIRST-STEP range=0  n_unique=1 | FULL range=0.0634
```

The first-step vector is **constant** -- one unique value across all 32 candidates, on
every tick.

786a's `_spearman` guards against exactly this with `if np.std(rb) == 0.0: return None`,
but **the guard cannot fire**: it tests the std of the *ranks*, and double-argsort of a
constant vector returns a permutation of `0..K-1` (std 9.23 at K=32), not a constant. So
the Spearman was computed between the true full-horizon ranking and an arbitrary
stable-sort tie-break ordering -- noise centred on zero, giving `recruitment ~ 1.0`.

Simulating that directly (`spearman(random_full, constant_first)` over 200 draws) yields
**mean 1.0173, sd 0.1871**. The manifest's seed-0 familiar condition reports
`recruitment_rate = 1.01725`, with per-layout `recruitment_sd` of 0.149 / 0.207 / 0.165 /
0.190. The match is to five significant figures on the mean.

**Consequence.** 786a's recruitment DV measured tie-break noise, not recruitment. A flat
between-condition delta is what that produces *by construction*, so the flat null is an
artifact of the DV and not a reading about arbitration. 786a's
`candidate_score_range_non_degenerate` readiness check only gated the **full-horizon**
vector's range, which is why the run passed readiness with the first-step vector
degenerate.

**What this does NOT settle.** Whether MECH-163's `weakens` should stand, and whether
786a should be re-adjudicated `non_contributory` on a measurement defect (as 786 was),
is `/failure-autopsy` and `/governance` work. Recorded here, applied nowhere.

**What it changes for SD-081.** The falsifier's OFF arm cannot simply be 786a as-run:
its DV is degenerate, so it is not a usable baseline. Both arms must be re-run with a
non-degenerate habit read. `dualsystem_habit_depth` is floored at 2 in
`_arbitrate_dual_system` so the degenerate depth is unreachable by config.

## Architecture Context

**Distinct from ARC-071.** ARC-071 is the **transfer** mechanism (planned -> habitual
chunking; slow, repetition-driven, moves content between pathways). SD-081 implements
the **allocation** mechanism (which pathway holds control right now; fast,
uncertainty-driven). MECH-163 presupposes both and specifies neither. ARC-071 remains
unbuilt and this SD does not build it -- and does not need it, because allocating
between two existing pathways does not require content to have been pumped between them.

**Not gated by ARC-007 STRICT.** The arbitrator re-weights the *scoring* of value-flat
hippocampal proposals; it does not seed them.

## What This SD Enables

- The MECH-477 falsifier: a two-arm arbitrator OFF vs ON re-run of the 786a design,
  holding the familiarity manipulation and the AUC manipulation-check bar (>= 0.7) fixed,
  and carrying the mandatory arbitration-weight-varies-with-uncertainty check.
- A MECH-163 leg (1) retest on a substrate that can express differential recruitment.

## Constraints

- **No learned parameters.** The arbitrator is a read-only weighting over existing
  scorers -- no encoder head, no gradients, so **no P0/P1/P2 phased training is
  required.** Deliberately not a learned gate: Daw's arbitration is normative Bayesian,
  and a learned gate would confound "the arbitrator works" with "the gate trained".
- **MECH-094 does not apply.** Nothing is written to memory; no simulated or replayed
  content is produced, so `hypothesis_tag` has no locus here.
- **Default OFF and bit-identical.** With the flag off the block is skipped entirely: no
  second scoring pass, no familiarity query, `last_arbitration` stays `None`.

## Related Claims

MECH-477 (the claim this substrate exists to falsify), MECH-163 (leg 1),
ARC-071 (transfer -- distinct, still unbuilt), ARC-007, ARC-016, MECH-112.
