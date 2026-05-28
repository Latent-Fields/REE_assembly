# MECH-341: E3 Score Diversity Preservation

**Claim ID:** MECH-341
**Subject:** ethics_engine_3.scoring_trajectory_class_diversity_preservation
**Status:** IMPLEMENTED 2026-05-27
**Registered:** 2026-05-25
**Depends on:** ARC-065, ARC-033, SD-003 (superseded; counterfactual evaluation retained via MECH-256 + SD-029 + MECH-257), INV-076
**Blocks (now unblocked):** R2.c rule in `evidence/planning/behavioral_diversity_isolation_plan.md`; Q-054 (entropy floor for ARC-062 context discriminator); behavioural arm of `arc_062_rule_apprehension:GAP-B` (V3-EXQ-543l successor cohort).

## Problem

ARC-065 commits to a four-substrate distributed diversity-generation pathway
(LC-NE tonic noise, frontopolar curiosity, striatal novelty, hippocampal
trajectory sampling), all at the proposal layer (Layer A). The post-CEM
scoring step at E3 had no corresponding diversity-preservation mechanism.
V3-EXQ-608 P2 (`v3_exq_608_mech341_e3_score_collapse_diagnostic`, run
2026-05-26T02:58Z) operationalised the gap: across 3 seeds, with the
SP-CEM main-path landed and consistently delivering `frac_pre_ge2 = 1.0`
(≥ 2 first-action classes in the candidate pool every measured tick), E3
scoring collapsed to a single first-action class with
`mean_top2_class_gap ∈ [0.27, 0.60]` (LARGE-gap collapse; 2/3 seeds
fired `R2a_e3_collapse_confirmed_large_gap`).

Per the isolation plan section "Substrate design options for MECH-341":

> Option 3 (jittered tie-breaking near top) is structurally insufficient
> when the collapse happens at large score gaps. EXQ-608's
> `frac_e3_collapse_above_eps ∈ [0.76, 0.99]` rules it out. Options 1
> (entropy bonus over candidate first-action classes added to E3 score)
> and 2 (class-stratified argmax with within-class proportional sampling)
> are the routes.

## Solution

Both options landed under one master switch, with independently togglable
sub-flavours mirroring the MECH-314a/b/c precedent. Q-054 falsifier (a
subsequent `/queue-experiment` session) can dissociate which one carries
the load.

**Module:** `ree-v3/ree_core/predictors/e3_score_diversity.py` (`E3ScoreDiversity`,
`E3ScoreDiversityConfig`, `E3ScoreDiversityDiagnostics`, `build_from_ree_config`).

Pure-arithmetic regulator. No `nn.Module` inheritance. No learned parameters.
Sibling pattern to MECH-313 NoiseFloor, MECH-314 StructuredCuriosity,
MECH-320 TonicVigor.

### Option 1: Entropy bonus

`apply_entropy_bonus(scores, candidates, simulation_mode=False) -> Tensor[K]`

1. Per-candidate first-action argmax class index.
2. Per-class frequency `p_c = count(c) / K`.
3. Per-candidate bonus = `entropy_lambda * p_c` (REE lower-is-better
   convention; positive bonus penalises over-represented classes).
4. Clamp to `[-entropy_bias_scale, +entropy_bias_scale]`.

Returns zeros when (a) sub-flavour is off, (b) `simulation_mode=True`
(MECH-094 gate), (c) `K < 2`, or (d) every candidate shares one class
(no homogenisation gradient available).

Composed into `scores` AFTER the existing score_bias chain (dACC /
lateral_pfc / ofc / mech295 / curiosity / tonic_vigor) and BEFORE the
`last_scores` write and softmax. Diagnostics capture the post-MECH-341
score state.

### Option 2: Class-stratified selection

`stratified_select(scores, candidates, simulation_mode=False) -> Optional[int]`

1. Partition candidates by first-action class.
2. Per class, pick the `argmin`-score candidate as the class representative.
3. Softmax across class-representatives with temperature
   `stratified_temperature`.
4. Sample a class-representative and return its global candidate index.

Returns `None` (caller falls through to legacy `argmin`) when sub-flavour
is off, `simulation_mode=True`, or fewer than
`min_classes_for_stratification` unique first-action classes are present.

Replaces `scores.argmin()` in the committed selection path of
`E3TrajectorySelector.select`. The uncommitted (multinomial) path inherits
the Option 1 bonus through `probs` but does not invoke
`stratified_select` — uncommitted selection is already stochastic by
design.

## Architecture Context

| Layer | Mechanism | Substrate status |
|-------|-----------|------------------|
| A — Proposal | ARC-065 SP-CEM (LC-NE / curiosity / novelty / hippocampal sampling) | landed 2026-05-17 main-path |
| **B — Scoring** | **MECH-341 (this claim)** | **landed 2026-05-27** |
| C — Action selection | MECH-313 NoiseFloor (softmax temperature lift); SD-032 cingulate cluster | landed |
| D — Representation | MECH-269 V_s / MECH-284 staleness | landed |

`E3Selector.select` composition order at the call site
(`agent.py:select_action`):

```
scores = mean_per_candidate(score_trajectory(candidates))
scores += dacc_score_bias              # composed bias chain:
                                       #   dACC (SD-032b)
                                       # + lateral_pfc (SD-033a)
                                       # + ofc (SD-033b)
                                       # + gated_policy (ARC-062)
                                       # + mech295_liking_bridge
                                       # + curiosity (MECH-314)
                                       # + tonic_vigor (MECH-320)
                                       # + forced_score_bias (V3-EXQ-563)
scores += apply_entropy_bonus(...)     # MECH-341 Option 1 (NEW)

last_scores = scores.detach()
probs = softmax(-scores / effective_temperature)   # MECH-313 lifts temperature

if committed:
    selected_idx = stratified_select(...) or scores.argmin()   # MECH-341 Option 2 (NEW)
else:
    selected_idx = multinomial(probs, 1)
```

## Config

`REEConfig.from_dims(...)` surface:

| Param | Type | Default | Purpose |
|-------|------|---------|---------|
| `use_e3_score_diversity` | bool | `False` | Master switch; bit-identical OFF |
| `use_e3_diversity_entropy_bonus` | bool | `True` | Option 1 sub-flavour |
| `use_e3_diversity_stratified_select` | bool | `True` | Option 2 sub-flavour |
| `e3_diversity_entropy_lambda` | float | `0.05` | Bonus weight; Q-054 calibrates |
| `e3_diversity_entropy_bias_scale` | float | `0.1` | Per-candidate clamp; mirrors lateral_pfc / curiosity / tonic_vigor `bias_scale` |
| `e3_diversity_stratified_temperature` | float | `1.0` | Softmax temperature across class representatives; orthogonal to MECH-313 |
| `e3_diversity_min_classes_for_stratification` | int | `2` | Below this, stratified_select falls through to argmin |

Both sub-flavour flags are consulted ONLY when the master is `True`.
Master OFF means `agent.score_diversity is None` and every wired call site
is bypassed.

## What This SD Enables

- **R2.c rule** (`behavioral_diversity_isolation_plan.md`): if
  `B_only` arm produces `trajectory_class_count >= 2` with
  `first_action_entropy > 0.3`, MECH-341 promotion to provisional.
- **Q-054** falsifier becomes well-posed: the substrate exists to test
  whether the ARC-062 context discriminator has enough class-entropy lift
  to learn a discriminative cut between reef and foraging contexts.
- **`arc_062_rule_apprehension:GAP-B`** behavioural follow-on: the
  V3-EXQ-543l mixed-evidence outcome can be retested under a substrate
  that no longer collapses diversity at the scoring step.
- **Layer-B isolation arms**: the full 11-arm matrix
  (`{A,B,C,D}_only / ablate_X / ALL_ON`) becomes runnable; previously
  every arm involving B was non-contributory by construction.

## Falsifiability

Per the isolation plan and the EXQ-608 failure record, MECH-341 is
falsifiable on two axes:

1. **Substrate readiness (V3-EXQ-611, queued in this landing session):**
   diagnostic ablation across `ALL_OFF` baseline / `OPT1_ONLY` /
   `OPT2_ONLY` / `BOTH_ON` arms on the EXQ-608 env. Acceptance criteria
   reuse the EXQ-608 metric stack. PASS = `selected_action_classes_count ≥ 2`
   with `frac_pre_ge2 ≥ 0.5` in either single-option arm.
2. **Behavioural impact (deferred to follow-on EXQ):** Phase P3
   `B_only / ablate_B / ALL_ON` arms on a downstream env (CausalGridWorld
   or SD-054 reef). Apply R2.c rule on landing.

## Phased Training

Not applicable. Pure-arithmetic regulator; no learned parameters; no
gradient flow. Q-054 calibration of `entropy_lambda` is a parametric
sweep, not a phased latent-target training protocol.

## MECH-094 Compliance

Both methods accept `simulation_mode: bool = False`; when True,
`apply_entropy_bonus` returns `zeros[K]` and `stratified_select` returns
`None` (caller falls through to legacy argmin). The diagnostic counter
`n_simulation_skipped` tracks both paths.

The wired call site (`E3Selector.select`, invoked from
`REEAgent.select_action`) is a waking path — `simulation_mode=False` is
passed explicitly. The inline gates are defensive against future
consumers (replay / DMN / ghost-goal probes if they ever invoke E3
selection directly).

## ML/AI Engineering Notes

The engineering problem is large-gap argmax collapse on a categorical
action axis when the score function is continuous on a richer (z_world)
space.

- **Option 1** maps to Mnih 2016 A3C-style entropy regularisation, with
  the REE-specific adaptation that `H(class | candidates)` is computed
  across the candidate pool's first-action argmaxes (a *local* categorical
  axis), not over the executed policy. Coverage-criterion in the MERL
  sense; not soft-actor-critic global policy entropy.
- **Option 2** maps to stratified sampling / balanced minibatch
  construction in active learning, with the REE-specific adaptation that
  the stratification axis is the categorical first-action class and the
  per-class representative is the best-scoring candidate (preserves
  dominance ordering within each class).

Failure modes defended against:

- **Entropy dominating the harm score in well-resourced regimes.**
  Mitigated by `entropy_lambda=0.05` default (small) and the
  `entropy_bias_scale=0.1` clamp matching the rest of the score-bias
  chain. Substrate is OFF by default; flag must be set explicitly.
- **Stratified sampling admitting low-quality candidates from sparse
  classes.** Mitigated by "best within each class" — sparse classes only
  send their best representative; dominated-by-other-class candidates are
  never sampled.
- **`stratified_temperature=0` collapse.** Floored at `1e-6` inside
  `stratified_select`.

Biological compatibility: Rigotti et al. 2013 (mixed selectivity in PFC
encodes diverse trajectory contingencies; preservation across scoring
layers required for downstream flexibility) and Padoa-Schioppa & Conen
2017 (OFC value comparison preserves option-distinct value signals).
Both options are valid biological renderings; Option 1 is the soft-bias
reading, Option 2 is the categorical-preservation reading. The
togglable-both architecture lets the Q-054 falsifier dissociate them
empirically.

## Related Claims

- **MECH-341** (this claim)
- **ARC-065** — parent diversity-generation pathway; Layer A
- **MECH-313 / MECH-314 / MECH-318 / MECH-319** — sibling ARC-065 / ARC-064
  child substrates at the proposal / action-selection layers
- **Q-054** — minimum trajectory-class diversity floor for ARC-062
- **INV-076** — diversity as structural prerequisite for ethical
  counterfactual evaluation
- **ARC-062** — rule apprehension via gated policy; GAP-B downstream
  beneficiary
- **SD-003** (superseded) — counterfactual pipeline retained via
  MECH-256 / SD-029
- **MECH-094** — hypothesis_tag invariant; call-site-scoped via
  `simulation_mode` kwarg

## Substrate Validation Status

| Phase | Status | Owner | Evidence |
|-------|--------|-------|----------|
| P1 substrate landing | DONE 2026-05-27 | this session | code + 506/506 contracts + 7/7 preflight PASS |
| P2 (substrate readiness) | FAIL 2026-05-27T13:02Z | V3-EXQ-611 | C1 false: ARM_1/3 entropy_max_abs 0.023-0.044 << gap range 0.27-1.96; ARM_2 n_stratified_fired=0 (committed branch never entered + Option-2 was committed-only) |
| Retune (2026-05-28) | DONE 2026-05-28 | implement-substrate-mech-341-retune | (a) e3_selector.py stratified_select call-site expanded to uncommitted branch; (b) V3-EXQ-611b 6-arm sweep queued (3 option groups x 2 entropy_bias_scale); 506/506 contracts PASS post-edit |
| P2 retune validation | queued | V3-EXQ-611b | TBD |
| P3 (B_only / ablate_B / ALL_ON behavioural) | gated on P2 retune PASS | TBD | TBD |
| Promotion to provisional | gated on R2.c rule | governance | TBD |

## Retune (2026-05-28)

V3-EXQ-611 FAILed substrate-readiness on both validation channels:

1. **Entropy bonus magnitude insufficient.** With
   `entropy_bias_scale=0.1` (the default at landing), the per-candidate
   bonus max_abs sat at 0.023-0.044 across the 3 OPT1/BOTH arms while
   the observed `mean_top2_class_gap` was 0.27-1.96. The substrate
   wired in and fired, but the magnitudes could not move selection
   ordering on a meaningful fraction of ticks.
2. **Stratified-select trigger never reached.** With the committed
   branch never entered during the V3-EXQ-611 measurement episodes
   (high `_running_variance` driving the uncommitted multinomial path),
   the prior implementation gated `stratified_select` to the committed
   branch only, producing `n_stratified_fired = 0` across all three
   seeds.

The retune lands two paired actions:

**(a) Call-site expansion** (substrate-side). `E3TrajectorySelector.select`
now consults `stratified_select` on BOTH the committed and uncommitted
selection paths. The Option-2 categorical-preservation semantic
(sample across class-representatives rather than across raw softmax
probabilities) applies whenever the candidate pool admits >= 2 unique
first-action classes, regardless of commit state. Bit-identical when
`score_diversity is None` or when `use_e3_diversity_stratified_select`
is False -- `stratified_select` returns `None` and the caller falls
through to legacy `argmin` (committed) or `multinomial` (uncommitted).
MECH-094 preserved via the existing `simulation_mode` kwarg. Smoke
verified the uncommitted-branch firing path; 506/506 contracts PASS
post-edit.

**(b) Parameter sweep** (validation-side). V3-EXQ-611b queues a 6-arm
factorial across 3 option groups (OPT1_only / OPT2_only / BOTH) x 2
`entropy_bias_scale` values (1.0 / 2.0). No config defaults change per
implement-substrate skill rule; the scales are passed via per-arm
cfg_overrides. ALL_OFF behaviour is established by the V3-EXQ-611
manifest already on origin/master (the retune sweep replaces the
ALL_OFF anchor with 6 informative ON arms).

Updated acceptance criteria:

- **C1 (call-site expansion).** `n_stratified_fired > 0` across all
  seeds in the 4 stratified-ON arms (ARM_3 / ARM_4 / ARM_5 / ARM_6).
  Direct test of the module-level retune.
- **C2 (bonus scale-commensurate).** `last_entropy_bonus_max_abs >=
  0.7 * scale` on the majority of seeds in the 4 entropy-ON arms.
  Substrate is putting the configured magnitude on the table.
- **C3 (selection-step diversity preserved).** At least one arm
  produces `selected_classes_count >= 2` AND `frac_pre_ge2 >= 0.5` on
  a majority of seeds.
- **C4 (informational ordering).** `scale=2.0 BOTH_ON >= scale=1.0
  BOTH_ON` selected-class entropy.
- **R2.c readiness.** At least one arm clears
  `mean_selected_class_entropy_nats >= 0.3`.

PASS gate: `>= 15/18` seeds complete AND C1 holds AND (C2 OR C3).

The interpretation grid in the V3-EXQ-611b script routes the next
governance walk per the four outcomes (PASS+C3 routes to behavioural
successor; FAIL with C1=false routes to /diagnose-errors; FAIL with
C1=true and C2/C3=false routes to algorithm-level substrate revisit).

## Plan-of-Record References

- `REE_assembly/evidence/planning/behavioral_diversity_isolation_plan.md`
  (status table row 2; substrate-design options section)
- `REE_assembly/docs/claims/claims.yaml` MECH-341 entry
- `ree-v3/ree_core/predictors/e3_score_diversity.py` (substrate
  implementation)
- `ree-v3/ree_core/predictors/e3_selector.py` (call sites)
- `ree-v3/ree_core/utils/config.py` (flat REEConfig flags +
  `from_dims` surface)
- `ree-v3/ree_core/agent.py` (instantiation in `REEAgent.__init__`;
  reset hook; e3.select kwarg pass-through)
