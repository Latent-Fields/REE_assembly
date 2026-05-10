# MECH-313: stochastic_noise_floor (LC-NE tonic / SAC max-entropy analog)

**Claim ID:** MECH-313
**Subject:** policy.stochastic_noise_floor_lc_ne_tonic_analog
**Status:** IMPLEMENTED 2026-05-10
**Registered:** 2026-05-10
**Parent cluster:** ARC-065 behavioral_diversity_generation_pathway
**Sibling claim:** MECH-314 structured_curiosity_bonus (separate substrate; not implemented in the same session)
**Related:** MECH-260 (state-dependent dACC anti-recency; Q-045 falsifies whether they collapse)
**Depends on:** ARC-065 (parent), MECH-104 (LC-NE phasic spike, already implemented; MECH-313 is the tonic complement)
**Blocks:** Q-043 weight calibration sweep, Q-045 4-arm collapse ablation (MECH-313 vs MECH-260)

---

## Problem

EXQ-433/433a/433b/470/523/523a/523b were reclassified `non_contributory`
because monomodal policy could not generate balanced agent-vs-env event
distributions for the SD-029 C2/C3 measurement gate. EXQ-543 (ARC-062
Phase 2a falsifier) was reclassified `non_contributory` 2026-05-10 for
the same family of reasons. The proposed ARC-064 cluster (bottom-up
rule discovery) presupposes behavioural diversity exists in the
trajectory record; ARC-062 (top-down rule application) presupposes
context to detect. Without an upstream behavioural diversity
generator, neither pathway has anything to weight or cluster.

The Pull 1 lit-pull (`evidence/literature/targeted_review_arc_065_behavioral_diversity_generation/SYNTHESIS.md`,
9 entries, lit_conf 0.78-0.82) settled four falsifiable questions and
identified TWO load-bearing missing substrates:

- **MECH-313 stochastic_noise_floor** (this claim) -- LC-NE tonic
  analog. State-independent softmax-temperature lift. Wilson 2014 /
  Faisal 2008 / Aston-Jones & Cohen 2005 anchors.
- **MECH-314 structured_curiosity_bonus** (sibling claim, separate
  substrate, not in this session) -- frontopolar exploration analog.
  Daw 2006 / Friston 2015 anchors.

Pull 1 R1 verdict (BOTH-CHANNELS-NEEDED, conf 0.85): single-channel
readings fail empirically (noise-only) or biologically (curiosity-only).
Pull 1 R2 verdict assigned LC-NE tonic to LOAD-BEARING. Pull 1 R4
verdict assigned MECH-313 to **continuous** computation (every tick,
regardless of context).

---

## Solution

### Module

`ree-v3/ree_core/policy/noise_floor.py` -- `NoiseFloor` class +
`NoiseFloorConfig` dataclass. Pure-arithmetic, no learned parameters,
no `nn.Module` inheritance. Lives in `ree_core.policy.__init__`
alongside `GatedPolicy` (the ARC-062 weak-reading rule-apprehension
sibling, also a policy-layer module).

### Algorithm

Per waking tick:

```
effective_T = max(baseline_T + noise_floor_alpha, noise_floor_min_temperature)
```

- `noise_floor_alpha`: SAC-entropy-bonus analog (Haarnoja et al. 2018
  soft actor-critic temperature). Constant additive lift on the
  softmax temperature.
- `noise_floor_min_temperature`: hard floor on the effective
  temperature so the policy never collapses to argmax even under
  annealing schedules that drive the baseline below 1.0.

Both lift the softmax temperature only. There is no candidate-level
bias and no perturbation of scores. The action-selection mechanism is
unchanged; the regulator is a pure scalar transform.

### Config

`REEConfig` (`ree-v3/ree_core/utils/config.py`):

| Param | Type | Default | Purpose |
|-------|------|---------|---------|
| `use_noise_floor` | bool | False | master switch (no-op default) |
| `noise_floor_alpha` | float | 0.1 | SAC-entropy-bonus analog; additive temperature lift |
| `noise_floor_min_temperature` | float | 1.0 | hard floor; matches existing E3 baseline |

All wired through `REEConfig.from_dims()`. Defaults are conservative
starting points; Q-043 calibrates magnitudes via parametric sweep on
V3-EXQ-543b/c.

### Data flow

```
REEAgent.select_action()
  -> noise_floor.compute_effective_temperature(temperature, simulation_mode=False)
  -> e3.select(candidates, effective_temperature, ...)
```

The integration point is the `e3.select(...)` call site in
`select_action()`. Phase 1 wires the regulator at the call site only;
no candidate-level changes, no E3 internal modification.

### Backward compat

- Master flag default OFF -> `agent.noise_floor` is None ->
  select_action passes `temperature` unchanged to `e3.select` ->
  bit-identical to baseline.
- All existing experiments unaffected.

### Phased training

Not applicable. Pure scalar regulator. No learned parameters. No
gradient flow.

### MECH-094

`compute_effective_temperature(simulation_mode=True)` returns the
baseline temperature unchanged and increments only the simulation-skip
counter. Match the SD-035 amygdala / MECH-279 PAG / `gated_policy`
simulation_mode pattern. The `select_action` call site passes
`simulation_mode=False` (waking action selection); replay / DMN
consumers (none today; reserved for forward-compat) get the unmodified
baseline so simulation paths cannot inherit the waking-tonic noise
floor that biologically belongs only to active behaviour.

---

## Distinction from MECH-260

| Aspect | MECH-260 (dACC anti-recency) | MECH-313 (stochastic noise floor) |
|--------|------------------------------|-----------------------------------|
| Site | Per-candidate `score_bias` | Softmax temperature |
| State | State-dependent (recent action history FIFO) | State-independent (no history read) |
| Mechanism | Penalises recently-selected action class | Lifts entropy uniformly |
| Biology | dACC + lateral aPFC anti-recency suppression (Scholl & Klein-Flugge 2018) | LC-NE tonic firing (Aston-Jones & Cohen 2005) |
| After argmax-on-A behaviour | Penalises class A specifically | Raises probability mass on every NON-A class equally |
| ML analog | Anti-recency / novelty bonus | SAC max-entropy regularisation (Haarnoja 2018) |

Q-045 falsifies whether they collapse into a single substrate via a
4-arm ablation (both-OFF / 313-only / 260-only / both-ON). The
substrate guarantees they can coexist as independent flags.

---

## Lit-pull verdicts

Pull 1 SYNTHESIS (`evidence/literature/targeted_review_arc_065_behavioral_diversity_generation/SYNTHESIS.md`,
9 entries, lit_conf 0.78-0.82, supports-direction):

- **R1 BOTH-CHANNELS-NEEDED** (conf 0.85): noise-floor (this claim) AND
  structured-curiosity (MECH-314) both required. Wilson 2014 Horizon
  task + Faisal/Selen/Wolpert 2008 noise-substrate irreducibility +
  Friston 2015 active-inference complementary terms. Single-channel
  readings fail.
- **R2 LC-NE tonic LOAD-BEARING** (conf 0.84): Aston-Jones & Cohen 2005
  adaptive-gain model. Tonic mode elevates baseline decision noise
  across all policies. MECH-104 covers the phasic spike (already
  substrate-landed); MECH-313 is the tonic complement.
- **R3 PROMOTE-TO-CLUSTER** (conf 0.82): MECH-313 cannot fold into
  ARC-051 wanting hierarchy (anatomically distinct frontopolar+IPS vs
  striatum+vmPFC pathways per Daw 2006) or MECH-260 (which is
  *contributory* anti-recency, not active diversity generation).
- **R4 continuous, every tick** (conf 0.80): non-zero softmax
  temperature on E3 every waking tick, regardless of context.
  Aston-Jones & Cohen 2005 + Friston 2015. NOT triggered.

Magnitudes are NOT settled by the lit-pull. Q-043 captures the open
question of relative weight calibration via parametric sweep on
V3-EXQ-543b/c.

---

## Validation

### Substrate-readiness diagnostic

V3-EXQ-544 (`v3_exq_544_mech313_noise_floor_substrate_readiness.py`).
Five sub-tests UC1-UC5:

- UC1 forward-pass instantiation
- UC2 master-OFF backward-compat (agent.noise_floor is None)
- UC3 effective_temperature lift correctness (alpha + floor arithmetic)
- UC4 select_action wiring contract (e3 receives the lifted temperature)
- UC5 MECH-094 simulation gate

`experiment_purpose=diagnostic`. Substrate readiness only; behavioural
validation lands as Q-045 4-arm ablation (MECH-313 OFF / 313 only /
260 only / both ON) on V3-EXQ-543b/c successors AFTER substrate is in.

### Behavioural validation (downstream, NOT this session)

- Q-043 weight calibration sweep on `noise_floor_alpha` and
  `noise_floor_min_temperature`.
- Q-045 4-arm ablation (MECH-313 vs MECH-260 collapse falsifier).

---

## What this SD enables

- ARC-065 behavioral_diversity_generation_pathway: completes one of two
  load-bearing children identified by Pull 1 (the other is MECH-314
  structured_curiosity_bonus, a separate substrate task).
- V3-EXQ-543b/c successors that need behavioural diversity AS INPUT
  (not as output) -- including the rebalanced 4-arm Q-045 ablation
  experiment.
- Sleep-substrate refinement experiments (V3-EXQ-418m / 436b / 500b /
  503b per the 2026-05-10 reclassification cohort) that need
  non-degenerate waking diversity for sleep to refine.

---

## Out of scope (deferred)

- MECH-314 / MECH-314a/b/c structured_curiosity_bonus substrate
  (separate spawned task; sibling under ARC-065).
- MECH-318 / MECH-319 substrates (separate spawned tasks).
- Q-045 4-arm ablation experiment itself (queued AFTER substrate
  landing).
- Q-043 parametric sweep (downstream from Q-045 if MECH-313 is shown
  load-bearing).

---

## Related claims

- **ARC-065** (parent architectural commitment)
- **MECH-260** (related mechanism; Q-045 falsifies whether they collapse)
- **MECH-104** (LC-NE phasic spike; already substrate-landed; MECH-313 is the tonic complement)
- **MECH-314** (structured_curiosity_bonus sibling under ARC-065; separate substrate)
- **Q-043** (relative weight calibration -- parametric sweep)
- **Q-044** (MECH-314a/b/c sub-flavour independence -- sibling)
- **Q-045** (MECH-313 vs MECH-260 collapse falsifier -- 4-arm ablation)
- **MECH-094** (simulation_mode argument; call-site scoping for waking-only effects)
