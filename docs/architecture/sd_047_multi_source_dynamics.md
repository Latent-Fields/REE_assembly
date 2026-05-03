---
nav_exclude: true
---

# SD-047: Multi-Source Environmental Dynamics

**Claim ID:** SD-047
**Subject:** `environment.multi_source_dynamics`
**Status:** candidate (v3_pending)
**Registered:** 2026-05-03
**Origin:** Substrate-roadmap M-priority #4 (`docs/architecture/substrate_roadmap.md`).
Trigger: V3-EXQ-506 (2026-05-03) confirmed the substrate-ceiling signature flagged
in MECH-095's evidence_quality_note (2026-05-02) — the agency-detection comparator
PASSes the agent-vs-correlated condition (C4) but fails the agent-vs-env, agent-vs-
collateral, and env-vs-correlated conditions (C1-C3). The diagnosis is that
CausalGridWorldV3's "other-caused" change is too thin a causal background for the
comparator to learn a robust not-self baseline.
**Depends on:** MECH-095, SD-022

---

## Problem

CausalGridWorldV3's "other-caused" state change consists of three sources only:

- **Hazard drift** — deterministic per-tick step on the scheduled-hazard field.
- **Resource respawn** — stochastic timer-driven respawn after consumption.
- **Scheduled hazard injection** — fixed per-episode hazard placement.

This is a thin causal background. For agency-detection-comparator claims like
MECH-095, the agent's counterfactual signature
`E2_harm_s(z_t, a_actual) - E2_harm_s(z_t, a_cf)` only separates from
environmental noise when there *is* environmental noise. With sparse, scheduled
events, the comparator may match in narrow regimes (V3-EXQ-047k PASS, narrow
contact-recall window) but fails in the broader landscape (V3-EXQ-506:
agent vs env, agent vs collateral, env vs correlated all collapse). The
substrate is too clean — agent action accounts for most of the per-tick change,
and the comparator can satisfy C4 (agent-caused vs env-correlated) trivially
while still missing the structural distinction the claim requires.

The same thinness limits MECH-098 (reafference cancellation, which is
*for* noisy multi-source backgrounds) and MECH-099 (downstream agency
attribution, which has nothing meaningful to attribute when env-causation
is sparse and scheduled).

**Architectural reading:** these are not claim errors; they are substrate-
ceiling failures. The claims are V3-tractable in principle but the
substrate's causal vocabulary is too narrow. This is the diagnosis
captured by `epistemic_category: substrate_ceiling` in Phase 3 wave 2.

---

## Mechanism

SD-047 adds three concurrent stochastic event sources to CausalGridWorldV3,
each operating at a distinct spatial / temporal scale so the comparator
must learn structural agent-vs-env signatures rather than a single
filterable noise pattern.

### Source 1: Spatial perturbation field (weather analog)

A slowly-evolving 2D scalar field that perturbs per-cell hazard intensity.
Implementation: AR(1) noise on a coarse spatial grid (e.g. 4x4 super-cells
covering the 8x8 world), updated per tick with autocorrelation
`alpha_weather` (default ~0.95 -- slow drift). Perturbation magnitude
scaled to `sigma_weather` so the per-tick change in hazard intensity is
small relative to scheduled hazard appearance but persistent across
hundreds of ticks.

**Signature:** continuous-valued, spatially smooth, temporally
autocorrelated, agent-independent.

### Source 2: Probabilistic transient events (trap analog)

A low-rate Poisson process producing transient per-cell hazard
appearances and disappearances independent of agent action.
Per-tick per-cell appearance probability `p_transient_appear` (default
~1e-3 -- ~1 transient per ~12 cells per episode at 8x8) and per-tick
disappearance probability `p_transient_disappear` (default ~0.1 -- mean
lifespan ~10 ticks).

**Signature:** discrete, spatially-pointwise, temporally short-lived,
agent-independent.

### Source 3: Background drift sources

A small number `n_drift_sources` (default 1-2) of independent moving
objects following their own dynamics. Each drift source occupies a
single cell and steps with its own random-walk / drift policy
(`drift_policy: random_walk | linear_drift | levy_walk`).

**Signature:** discrete, mobile, temporally autocorrelated, agent-
independent.

### Why three sources?

A single noise source can be cancelled by a simple temporal or spatial
filter. Three sources at different scales force the comparator to learn
*structural* signatures of agent-causation vs env-causation -- which is
the claim under test. The agent action remains the discrete, focal,
agent-controlled signal class; multi-source dynamics provide the not-
self baseline against which agency detection is meaningful.

### Calibration target

When enabled, env-caused state-change events should occur at roughly
comparable rate to agent-caused state changes per episode (target:
1:1 to 2:1 env:agent change events). Below that, the comparator
trivially satisfies its criteria; above it, the agent's own signal is
overwhelmed and policy learning collapses. Calibration is empirical
(set per-source intensity parameters so an episode of random-policy
agent produces ~equal env-caused and agent-caused state-change ticks).

---

## Child mechanisms (deferred)

If SD-047 is implemented and validated, child claims register the
distinct signal classes:

### MECH-(TBD): spatial-perturbation continuous-noise class
- **Statement:** Continuous, smooth, autocorrelated env-caused state
  change forms a signal class distinct from action-caused state change
  along smoothness and autocorrelation features.
- Used by MECH-098 reafference cancellation as the "afference noise"
  channel.

### MECH-(TBD): transient-event discrete-noise class
- **Statement:** Discrete, spatially pointwise, short-lived env-caused
  state change forms a signal class distinct from action-caused state
  change along sparsity and lifespan features.
- Used by MECH-095 agency-detection comparator as the principal
  not-self baseline.

These children are deferred to the implementation phase -- registering
them now without an implementation invites the same overreach pattern
that produced SD-003's premature elaborate scaffolding (28 FAILs
before substrate caught up).

---

## Architecture context

SD-047 sits at the **environmental substrate** layer, parallel to
SD-022 (body-damage substrate), SD-029 (scheduled external hazard),
SD-035 (amygdala analog stream substrate). It does *not* modify the
agent or any internal latent: it changes only what the env feeds the
agent through `obs_dict` and the underlying hazard field.

**Distinct from V4 multi-agent ecology.** Full social / multi-agent
substrate (other agents whose causation is genuinely intentional) lives
in `v4_spec.md` (V4-1). SD-047 is the V3-tractable version: env causation
that is non-trivial but non-intentional. This is exactly the right level
for agency-detection comparator claims, which test the agent vs not-
agent distinction; the agent vs other-agent distinction is a separate
V4-bound claim.

**Distinct from differentiated coping channels (roadmap M-priority
#5 / SD candidate `environment.differentiated_coping_channels`).**
That SD addresses MECH-102's substrate-ceiling by giving the agent
multiple distinct intervention modalities. SD-047 addresses MECH-095's
substrate-ceiling by giving the env multiple distinct causal sources.
Independently implementable.

---

## What this SD enables

**Primary unblock:**
- **MECH-095** (`substrate_ceiling`, `status: active`) — the TPJ agency-
  detection comparator can be honestly tested. Pre-registered
  prediction: under SD-047, V3-EXQ-506-equivalent C1-C3 conditions
  should PASS where they currently FAIL.

**Secondary unblocks:**
- **MECH-098** (reafference cancellation) — finally has a noisy-
  background test condition. Currently has no honest substrate.
- **MECH-099** (downstream agency attribution) — has something
  meaningful to attribute.

**Cleaner training distribution:**
- **E2_harm_s under SD-013 interventional loss** currently sees clean
  action-controlled vs scheduled-hazard transitions. SD-047 exposes it
  to mixed-causality transitions where attribution is genuinely
  ambiguous. The cf_gap_ratio bottleneck identified in V3-EXQ-330
  (cf_gap_ratio ~ 1.3-1.5x, target > 2.0x) may partly reflect the
  too-clean training distribution; SD-047 + SD-013 jointly is a
  candidate fix.

**Indirectly relevant:**
- **ARC-033** (sensory-discriminative harm forward model, status:
  provisional). The recent V3-EXQ-508 borderline FAIL flagged ARC-058
  (somatic/affective dissociation per Wager 2013, Hofbauer 2001) as a
  successor direction. Robust dissociation evaluation benefits from
  richer multi-source backgrounds.

---

## Validation experiment (deferred)

**Pre-registered protocol for SD-047 validation:**

A discriminative-pair experiment registered at substrate-implementation
time (next available EXQ slot). Two arms:

- **ARM_A (substrate ON):** `multi_source_dynamics_enabled=True` with
  default-calibrated per-source intensities. Run the same
  agency-comparator measurement as V3-EXQ-506: train E2_harm_s with
  SD-013 interventional loss, evaluate counterfactual_forward gap on
  four held-out conditions {agent-caused, env-caused, agent-collateral,
  env-correlated}.
- **ARM_B (substrate OFF):** `multi_source_dynamics_enabled=False`,
  identical seeds and hyperparameters. Expected to replicate
  V3-EXQ-506's C1-C3 FAIL pattern.

**Pre-registered prediction:**
- ARM_A C1, C2, C3 PASS (≥2/3 seeds each).
- ARM_B C1, C2, C3 FAIL (replicating EXQ-506).

**Interpretation:**
- ARM_A all-PASS + ARM_B all-FAIL → **SD-047 validated; MECH-095
  substrate_ceiling lifted; MECH-095 evidence_quality_note updated;
  MECH-095 evaluable under standard exp_conf gating.**
- ARM_A some-PASS + ARM_B all-FAIL → **partial unblock; refine
  per-source calibration.**
- ARM_A all-FAIL → **SD-047 implementation gap or substrate-ceiling
  diagnosis was wrong. Revisit MECH-095 architectural reading.**

This is a falsifiable substrate test, not just an exploratory sweep.

---

## Implementation surface

**ree-v3 / `ree_core/env/causal_grid_world_v3.py`** (or equivalent env
module):

```python
@dataclass
class WeatherFieldConfig:
    enabled: bool = False
    grid_super_cells: int = 4   # coarse grid resolution
    alpha_ar1: float = 0.95     # autocorrelation
    sigma: float = 0.05         # per-cell perturbation magnitude

@dataclass
class TransientEventConfig:
    enabled: bool = False
    p_appear: float = 1e-3
    p_disappear: float = 0.1
    intensity: float = 1.0

@dataclass
class BackgroundDriftConfig:
    enabled: bool = False
    n_sources: int = 1
    drift_policy: Literal["random_walk", "linear_drift", "levy_walk"] = "random_walk"

@dataclass
class MultiSourceDynamicsConfig:
    enabled: bool = False  # master switch; bit-identical OFF
    weather: WeatherFieldConfig = field(default_factory=WeatherFieldConfig)
    transients: TransientEventConfig = field(default_factory=TransientEventConfig)
    drift: BackgroundDriftConfig = field(default_factory=BackgroundDriftConfig)
```

**Bit-identical OFF requirement:** when `enabled=False`, the env's
internal RNG sequence and per-tick state-update path must match the
pre-SD-047 baseline exactly. Add the multi-source RNG draws inside an
`if cfg.enabled:` branch; do not draw RNG values that get discarded.
This preserves all existing experiment reproducibility.

**Per-source bit-identical OFF:** each sub-source can be enabled
independently for ablation studies (which source contributes most to
unblocking C1/C2/C3).

---

## Related claims

- **MECH-095** — substrate_ceiling claim this SD primarily unblocks.
  evidence_quality_note already documents the substrate-ceiling
  diagnosis (2026-05-02 annotation; 2026-05-03 V3-EXQ-506
  confirmation).
- **MECH-098** — reafference cancellation, currently lacks honest
  substrate.
- **MECH-099** — downstream agency attribution.
- **ARC-033** — provisional, would benefit from richer env for
  ARC-058 successor direction (Wager 2013, Hofbauer 2001 lit-pull).
- **SD-022** — body-damage substrate (depends_on; SD-047 layers on
  top of, does not replace).
- **SD-029** — scheduled external hazard (depends_on; SD-047 adds
  *unscheduled* env causation alongside).
- **`environment.differentiated_coping_channels`** (substrate-roadmap
  M-priority #5; not yet registered) — parallel SD addressing
  MECH-102's substrate_ceiling. Independently implementable.

## Lit-pull recommendation (pre-implementation)

Before substrate work begins, commission a focused lit-pull on:
- agency-detection under multi-source environmental noise
  (developmental + cognitive psychology on infant agency-perception
  in noisy environments)
- reafference cancellation under stochastic afference (cerebellum +
  parietal cortex)

This follows the "biology before formal definitions" rule
(`feedback_biology_before_formal_definitions.md`): SD-047 is
operationally simple but the *signature features* the comparator
should learn (smoothness, autocorrelation, sparsity, lifespan) are
empirical questions about how biological agency-detection actually
discriminates agent from non-agent. Skipping this risks a
philosophy-right / mechanism-wrong implementation that produces a
clean PASS on a wrong test.

Anchor candidates:
- Saxe & Carey 2006, Cog. Dev. (infant agency perception)
- Blakemore et al. 1998, Nat. Neurosci. (reafference cancellation
  cerebellar)
- Pitcher & Ungerleider 2021, TICS (lateral cortex agency network)
