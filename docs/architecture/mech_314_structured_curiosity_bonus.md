# MECH-314: structured_curiosity_bonus (frontopolar exploration / EFE analog)

**Claim ID:** MECH-314 (parent) + MECH-314a (striatal novelty) + MECH-314b (frontopolar uncertainty) + MECH-314c (learning progress)
**Subject:** policy.structured_curiosity_bonus_parent (parent) + 3 sub-flavours
**Status:** IMPLEMENTED 2026-05-10
**Registered:** 2026-05-10
**Parent cluster:** ARC-065 behavioral_diversity_generation_pathway
**Sibling claim:** MECH-313 stochastic_noise_floor (LC-NE tonic / SAC analog; substrate landed earlier the same day)
**Related:** MECH-318 / MECH-319 (separate spawned tasks, not landed in this session); MECH-104 (LC-NE phasic spike, already substrate-landed)
**Depends on:** ARC-065 (parent); MECH-313 (sibling noise-floor under same parent)
**Blocks:** Q-043 weight calibration sweep; Q-044 sub-flavour independence three-arm ablation; V3-EXQ-543c (curiosity + meta-RL recurrent baselines arm class)

---

## Problem

Pull 1 SYNTHESIS R1 verdict (BOTH-CHANNELS-NEEDED, conf 0.85):
behavioural diversity requires both a state-independent stochastic
floor (MECH-313) AND a state-dependent structured-curiosity bonus
(this substrate). MECH-313 landed earlier 2026-05-10. Without
MECH-314, the second load-bearing channel under ARC-065 is missing,
which means:

- Q-044 (sub-flavour independence -- are MECH-314a striatal novelty,
  MECH-314b frontopolar uncertainty, MECH-314c learning-progress
  three distinct substrates or three readings of one mechanism?) is
  unanswerable.
- V3-EXQ-543c (curiosity + meta-RL recurrent baselines arm class)
  has nothing to instantiate.
- The "structured" half of the explore-exploit decomposition Wilson
  2014 documents (directed information-seeking distinct from softmax
  decision noise) has no substrate.

The SYNTHESIS R3 verdict explicitly recommended NOT collapsing the
three sub-flavours prematurely (sub-MECH split rationale: heterogeneous
biological provenance, independent testability, distinct expected
failure signatures under ablation). That commitment is what makes
Q-044's three-arm ablation a meaningful empirical test rather than
re-litigation of the cluster registration.

---

## Solution

### Module

`ree-v3/ree_core/policy/structured_curiosity.py` -- `StructuredCuriosity`
class + `StructuredCuriosityConfig` dataclass. Pure-arithmetic, no
learned parameters, no `nn.Module` inheritance. Sibling to `noise_floor.py`
and `gated_policy.py` in the `ree_core.policy` package.

### Algorithm

Per waking `select_action` tick, given candidate first-step z_world
summaries `[K, world_dim]`, ResidueField (for 314a), and the
E3TrajectorySelector (for 314b):

```
total = zeros[K]                                                    # E3 lower-is-better
if 314a ON and residue_field has active centers:
    novelty[k] = min_i ||z_k - center_i|| over active centers
    total += -w_a * novelty / (mean_norm + 1e-6)                    # normalised, [K]
if 314b ON:
    unc = e3._running_variance                                      # scalar
    total += -w_b * unc * ones[K]                                   # broadcast
if 314c ON and lp_seeded:
    lp = ema_of(|PE_t - PE_{t-K}|)                                  # internal EMA scalar
    total += -w_c * lp * ones[K]                                    # broadcast
clamp total to [-bias_scale, +bias_scale]
return total                                                        # [K]
```

The bonus is non-positive everywhere any sub-flavour fires (curiosity
reduces a candidate's E3 score so it becomes more attractive under the
lower-is-better convention). Composed additively into `dacc_score_bias`
in `REEAgent.select_action()`, immediately after the MECH-295 liking-
bridge block and BEFORE the MECH-313 noise-floor temperature lift
(curiosity affects scores; noise floor affects temperature; orthogonal).

### Three sub-flavours

| Sub-claim | Biological anchor | Phase 1 signal source | Per-candidate? |
|-----------|-------------------|------------------------|----------------|
| **MECH-314a** striatal novelty | Wittmann et al. 2008 *Neuron* (ventral striatum novelty response independent of RPE) | min distance from candidate's first-step z_world to nearest ACTIVE ResidueField RBF center, normalised by candidate-pool mean norm | YES (genuinely [K]) |
| **MECH-314b** frontopolar uncertainty | Daw et al. 2006 *Nature* (rostrolateral PFC exploration bonus); Friston 2010/2015 EFE epistemic value | `e3._running_variance` scalar | NO (broadcast in Phase 1) |
| **MECH-314c** learning progress | Schmidhuber 1991 compression-progress; Pathak et al. 2017 forward-model PE | EMA of `|PE_t - PE_{t-K}|` where PE feed is `e3._running_variance` per tick | NO (broadcast in Phase 1) |

### Phase 1 honest scoping

314a is genuinely per-candidate. 314b and 314c are state-dependent
**global scalars broadcast across [K]** in Phase 1. The architectural
shape is correct (bonus magnitude varies with global uncertainty /
learning-progress; the substrate exposes the falsification surface),
and Q-044's three-arm ablation IS a flag-set decision -- the substrate
guarantees each sub-flavour can be turned on/off independently via
`use_curiosity_novelty / _uncertainty / _learning_progress` config
flags.

**What Phase 1 does NOT deliver:** distinguishable behavioural
signatures per sub-flavour at the candidate-selection level. With
broadcast-scalar 314b and 314c, ablating either of them shifts every
candidate's score by the same amount and does not change selection
ordering -- it can affect commit-threshold dynamics (since absolute
score magnitude matters there) but not which candidate wins under
softmax sampling. Per-candidate refinement of 314b (E1 forward-
variance head producing per-candidate uncertainty) and 314c (per-
candidate learning-progress estimate) is a Phase 2 follow-on, deferred
until Q-044's three-arm ablation surfaces concrete need.

The MECH-313 entry carries the analogous Phase-1 placement caveat
("whether the policy-layer regulators ultimately consolidate into one
module is OPEN pending MECH-314 / MECH-318 / MECH-319"); MECH-314 is
the second data point on that consolidation question.

### Config

`REEConfig` (`ree-v3/ree_core/utils/config.py`):

| Param | Type | Default | Purpose |
|-------|------|---------|---------|
| `use_structured_curiosity` | bool | False | master switch (no-op default) |
| `use_curiosity_novelty` | bool | True | MECH-314a switch (consulted only when master ON) |
| `use_curiosity_uncertainty` | bool | True | MECH-314b switch |
| `use_curiosity_learning_progress` | bool | True | MECH-314c switch |
| `curiosity_novelty_weight` | float | 0.05 | MECH-314a magnitude |
| `curiosity_uncertainty_weight` | float | 0.05 | MECH-314b magnitude |
| `curiosity_learning_progress_weight` | float | 0.05 | MECH-314c magnitude |
| `curiosity_bias_scale` | float | 0.1 | hard clamp on `|total bias|`; mirrors `lateral_pfc_bias_scale` |
| `curiosity_lp_ema_alpha` | float | 0.1 | 314c EMA smoothing (~10-tick window) |
| `curiosity_lp_window_k` | int | 5 | 314c `|PE_t - PE_{t-K}|` lag |

All wired through `REEConfig.from_dims()`. Sub-flavour switch defaults
are True (so flag-set Q-044 ablation is "turn the master ON, then flip
individual sub-flavours OFF"). Magnitudes are conservative starting
points; Q-043 (relative weight calibration MECH-313 vs MECH-314) and
Q-044 (sub-flavour independence) are the empirical resolution paths.

### Data flow

```
REEAgent.select_action()
  build per-candidate first-step z_world summaries [K, world_dim]
       (reused from lateral_pfc / ofc / mech295 chain when present)
  -> curiosity.compute_score_bias(summaries, residue_field, e3,
                                  simulation_mode=False) -> [K]
  -> dacc_score_bias += curiosity_bias  (additive composition)
  -> [MECH-313 noise_floor: temperature lift on baseline_T]
  -> e3.select(candidates, effective_temperature, ...,
               score_bias=dacc_score_bias)
  -> action

REEAgent.select_action(), AFTER e3.select:
  pe_scalar = e3._running_variance
  -> curiosity.update_prediction_error(pe_scalar, simulation_mode=False)
       (advances the 314c LP buffer for next tick)

REEAgent.reset() (per-episode):
  -> curiosity.reset()  (clears LP buffer + diagnostic counters)
```

### Backward compat

- Master flag default OFF -> `agent.curiosity` is None ->
  `select_action` skips the entire block and the LP feed -> bit-
  identical to baseline.
- All existing experiments unaffected. 273/273 contracts + preflight
  PASS with master OFF (regression-clean).

### Phased training

Not applicable. Pure-arithmetic regulator. No learned parameters. No
gradient flow. Defaults are seeded from the lit-pull magnitudes
discussion (Pull 1 SYNTHESIS); empirical calibration is Q-043 / Q-044
work post-substrate.

### MECH-094

Both `compute_score_bias(simulation_mode=True)` and
`update_prediction_error(simulation_mode=True)` honour the simulation
gate:

- `compute_score_bias(simulation_mode=True)` returns `zeros[K]` and
  increments only the simulation-skip counter.
- `update_prediction_error(simulation_mode=True)` is a no-op on the LP
  buffer (PE history does not advance on replay / DMN paths).

The `select_action` call site passes `simulation_mode=False` (waking
action selection). Match the SD-035 / MECH-279 / gated_policy /
MECH-313 simulation_mode pattern.

---

## Distinction from MECH-313

| Aspect | MECH-313 (stochastic noise floor) | MECH-314 (structured curiosity bonus) |
|--------|------------------------------------|----------------------------------------|
| Site | Softmax temperature kwarg into e3.select | score_bias kwarg into e3.select |
| State | State-INDEPENDENT | State-DEPENDENT (314a/b/c each in different ways) |
| Per-candidate | No (uniform temperature lift) | 314a yes; 314b/c broadcast scalar in Phase 1 |
| Mechanism | Lifts entropy uniformly across all classes | Reduces score for novel / uncertain / LP-rich candidates |
| Biology | LC-NE tonic firing | Frontopolar exploration + striatum novelty + intrinsic motivation |
| ML analog | SAC max-entropy regularisation | Count-based + uncertainty-driven + curiosity-driven RL bonuses |

Both can coexist independently: MECH-313 OFF + MECH-314 ON, MECH-313
ON + MECH-314 OFF, both-ON, both-OFF are all valid configurations.
Q-043 calibrates relative weights via parametric sweep on V3-EXQ-543b/c.

---

## Lit-pull verdicts

Pull 1 SYNTHESIS (`evidence/literature/targeted_review_arc_065_behavioral_diversity_generation/SYNTHESIS.md`,
9 entries, lit_conf 0.78-0.82, supports-direction):

- **R1 BOTH-CHANNELS-NEEDED** (conf 0.85): MECH-313 noise floor AND
  MECH-314 structured curiosity both required. Wilson 2014 Horizon
  task + Faisal 2008 noise irreducibility + Friston 2015 EFE
  complementary terms. Single-channel readings fail.
- **R2 multi-substrate distributed**: ARC-065 carries four substrate
  contributions; MECH-313 covers LC-NE tonic, MECH-314 covers
  frontopolar (314b) + striatum (314a) + intrinsic-motivation
  tradition (314c).
- **R3 PROMOTE-TO-CLUSTER + sub-MECH split** (conf 0.82 / 0.78):
  three sub-flavours registered as separate sub-claims rather than
  collapsed -- heterogeneous biological provenance + independent
  testability justify the split. Q-044 holds the resolution path.
- **R4 continuous-in-computation, triggered-in-dominance** (conf 0.80):
  bonus computed every tick; magnitude scales with model uncertainty
  / novelty. Phase 1 instantiation is fully continuous; Phase 2 may
  add an MECH-104 volatility-surprise gate on the 314b weight.

Lit anchors per sub-flavour:

- **MECH-314a**: Wittmann et al. 2008 *Neuron* (ventral striatum
  novelty response); Bellemare et al. 2016 NeurIPS (pseudo-count
  computational analog); Burda et al. 2018 ICLR (RND analog).
- **MECH-314b**: Daw et al. 2006 *Nature* (rostrolateral PFC
  exploration); Wilson et al. 2014; Friston 2010/2015 EFE
  decomposition; Houthooft et al. 2016 NeurIPS (VIME analog);
  Kidd & Hayden 2015 review.
- **MECH-314c**: Schmidhuber 1991 (compression progress); Pathak et
  al. 2017 ICML (curiosity-driven exploration via forward-model PE);
  Oudeyer et al. 2007 (intrinsic motivation systems / robotics).

Magnitudes are NOT settled by the lit-pull. Q-043 / Q-044 are the
empirical resolution paths.

Pull 1 explicitly flagged 314c as **least biologically anchored** ("no
clean cellular or regional analog"); the registration entry carries
the "potentially-discardable-if-314a+314b-suffice" note. Q-044's
resolution path includes that branch ("314c discardable" outcome:
retire 314c, keep a + b).

---

## Validation

### Substrate-readiness diagnostic

V3-EXQ-545 (`v3_exq_545_mech314_structured_curiosity_substrate_readiness.py`).
Five sub-tests UC1-UC5:

- UC1 forward-pass instantiation
- UC2 master-OFF backward-compat (`agent.curiosity` is None)
- UC3 each sub-flavour fires under flag-set isolation (314a-only,
      314b-only, 314c-only, all-off-master-on)
- UC4 select_action wiring contract (waking-call counter advances;
      bias lands additively in dacc_score_bias chain)
- UC5 MECH-094 simulation gate (compute_score_bias returns zeros +
      skip counter; update_prediction_error no-ops on LP buffer)

`experiment_purpose=diagnostic`. Substrate readiness only; behavioural
validation lands as Q-044 three-arm ablation on V3-EXQ-543b/c
successors AFTER substrate landing AND the MECH-318 / MECH-319
absorption-check sessions complete.

### Behavioural validation (downstream, NOT this session)

- **Q-043** weight calibration sweep on `(noise_floor_alpha,
  noise_floor_min_temperature, curiosity_*_weight)` -- parametric
  sweep on V3-EXQ-543b/c. PASS = consistent (w_313, w_314) regime
  across seeds with simultaneously high behavioural diversity AND
  task reward (Pareto frontier).
- **Q-044** three-arm ablation (314a-OFF, 314b-OFF, 314c-OFF +
  all-on baseline) on V3-EXQ-543b/c successors. Predicted distinct
  failure signatures per sub-flavour (per claim functional_restatement):
    - 314a-OFF: reduced return-rate to rarely-visited z_world
      regions.
    - 314b-OFF: reduced uncertainty-resolution rollouts at familiar-
      but-uncertain states.
    - 314c-OFF: reduced learning-curve curvature on tasks where
      model improvement rate varies with policy.
  Resolution outcomes: all three independent / 314c discardable /
  all collapse (per claim Q-044 notes).

---

## What this SD enables

- **ARC-065 behavioral_diversity_generation_pathway**: completes the
  second of two load-bearing children identified by Pull 1 (MECH-313
  noise floor was the first; MECH-314 structured curiosity is the
  second). With both substrates landed, ARC-065 carries the full
  cluster commitment.
- **V3-EXQ-543c** (curiosity + meta-RL recurrent baselines arm class)
  becomes substrate-landed and authorable. The curiosity arm of
  V3-EXQ-543c reads MECH-314a/b/c.
- **Q-044 three-arm ablation** is now a flag-set decision rather
  than a code-edit decision. The downstream session can author it as
  a single experiment script with three flag overrides per arm.
- **Q-043 weight calibration sweep** is now well-posed (both
  MECH-313 and MECH-314 substrates exist; parametric sweep can
  vary their weights).
- **Sleep-substrate refinement experiments** (V3-EXQ-418m / 436b /
  500b / 503b per the 2026-05-10 reclassification cohort) that need
  non-degenerate waking diversity for sleep to refine: the second
  ARC-065 substrate further reduces the risk of monomodal-collapse
  sleep-side artefacts.

---

## Out of scope (deferred)

- **MECH-318** (rule-state abstraction substrate -- ARC-064 child;
  flagged registration_provisional_pending_meta_rl_absorption_check)
  -- separate spawned task.
- **MECH-319** (simulation-mode rule-write gating; categorical replay
  tag at the arbitration layer) -- separate spawned task.
- **Q-044 three-arm ablation experiment itself** -- queued AFTER
  substrate landing AND the MECH-318 absorption-check session
  completes.
- **V3-EXQ-543c** (curiosity + meta-RL recurrent baselines arm class)
  -- queued downstream of MECH-318 absorption check.
- **Phase 2 per-candidate refinement of 314b/c** (E1 forward-variance
  head; per-candidate learning-progress estimate) -- deferred until
  Q-044 surfaces concrete need (i.e., a sub-flavour ablation produces
  weak signal because broadcast-scalar Phase 1 was insufficient).
- **MECH-104 volatility-surprise trigger gate on 314b weight**
  (Pull 1 R4 verdict's "triggered in dominance" arm) -- Phase 1 fully
  continuous; Phase 2 may add this gate.

---

## Related claims

- **ARC-065** (parent architectural commitment)
- **MECH-313** (sibling noise-floor under same parent; substrate
  landed earlier 2026-05-10)
- **MECH-314a** (striatal novelty sub-flavour; this substrate)
- **MECH-314b** (frontopolar uncertainty sub-flavour; this substrate)
- **MECH-314c** (learning-progress sub-flavour; this substrate;
  flagged potentially-discardable per Pull 1 R3 + Q-044)
- **MECH-104** (LC-NE phasic spike; already substrate-landed; sibling
  in the LC-NE substrate family)
- **MECH-260** (dACC anti-recency; related anti-monostrategy claim;
  Q-045 falsifies whether MECH-313 collapses with it)
- **Q-043** (relative weight calibration MECH-313 vs MECH-314)
- **Q-044** (sub-flavour independence three-arm ablation)
- **Q-045** (MECH-313 vs MECH-260 collapse falsifier)
- **MECH-094** (simulation_mode argument; call-site scoping for waking-
  only effects)
- **MECH-295** (liking-approach bridge; sibling score-bias contributor
  composed before MECH-314 in the chain)
- **MECH-318 / MECH-319** (sibling ARC-065 / ARC-064 substrates;
  separate spawned tasks)
