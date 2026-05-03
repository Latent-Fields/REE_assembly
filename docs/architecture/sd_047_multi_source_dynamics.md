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

**Pre-registered protocol for SD-047 validation — noise-level sweep:**

The original draft proposed a binary ON-vs-OFF discriminative pair.
The pre-implementation lit-pull (`evidence/literature/targeted_review_sd_047/`)
revised that protocol on two independent grounds. Both revisions are
load-bearing for interpretability.

**Revision 1: sweep, not binary** — Asai 2016 (DOI:
10.1016/j.psychres.2016.10.082) shows that agency judgment is a
non-monotonic function of the signal-to-noise ratio of self-originated
contribution to a continuously varying stimulus. Schizotypal
participants exhibit a shallower regression slope of agency rating
against self-other discriminability and produce both over- AND
under-attribution errors symmetrically depending on the S/N regime.
The implication for SD-047 is that the comparator's apparent competence
is non-monotonic in env noise level: too little env noise and the
comparator never sees the regime where slope is informative
(V3-EXQ-506 failure mode); too much and the agent's own signal is
overwhelmed and slope flattens again. A binary ON/OFF test is therefore
under-specified — a flat ON-vs-OFF result would be ambiguous between
"SD-047 works" and "SD-047 overshot calibration."

The corrected protocol is a multi-arm noise-level sweep at fixed
calibration parameters along all three sources. Suggested levels (to
be tuned at implementation):

- **ARM_0 (OFF baseline):** `multi_source_dynamics_enabled=False`.
  Expected to replicate V3-EXQ-506's C1-C3 FAIL pattern.
- **ARM_1 (low):** all sources at 0.25x default intensity.
- **ARM_2 (mid, default):** all sources at 1.0x default intensity
  (the calibration target: ~1:1-2:1 env:agent change events per ep).
- **ARM_3 (high):** all sources at 4.0x default intensity.

**Revised pre-registered prediction:**
- ARM_0 C1, C2, C3 FAIL (replication).
- C1, C2, C3 pass-rate forms an inverted U across ARM_1 → ARM_2 →
  ARM_3, peaking at or near ARM_2 (default calibration).
- Asai's slope analog (cf_gap_event / cf_gap_quiet ratio across the
  four held-out conditions) is highest at the U's peak and degrades
  symmetrically toward both extremes.

**Revision 2: explicit Woo/Spelke falsifier branch** — Woo, Liu, Spelke
2023 (DOI: 10.1111/desc.13453) showed that 3-month-old prereaching
infants attribute goal-directedness to others' reaching actions from
sparse, clean visual stimuli, before they themselves can reach. This
challenges the strong reading of substrate-ceiling: if clean stimuli
support agency attribution at very young ages, the discriminative
features that matter may be motion-contingency and goal-directedness
rather than smoothness/sparsity/lifespan. Those features are V4-bound
(genuine other-agents) rather than V3-tractable.

This routes a specific failure pattern to a specific architectural
diagnosis rather than to "SD-047 is broken."

**Revised interpretation grid:**

| ARM_2 outcome | ARM_0 outcome | Reading |
|---|---|---|
| C1, C2, C3 PASS | C1, C2, C3 FAIL | **SD-047 validated.** Substrate-ceiling diagnosis correct. Lift MECH-095 substrate_ceiling flag; mark MECH-098 evaluable; update evidence_quality_notes. |
| Inverted U with ARM_2 peak | Same as above | **SD-047 validated with calibration confirmation.** Asai non-monotonicity directly observed; default calibration is on the optimum. |
| ARM_1 or ARM_3 peaks instead of ARM_2 | C1-C3 FAIL | **SD-047 validated, calibration miscalibrated.** Recalibrate per-source intensities; do not draw architectural conclusions from this run. |
| Flat curve, all arms FAIL | C1-C3 FAIL | **Falsification of substrate-ceiling diagnosis as smoothness/autocorrelation/sparsity feature gap.** This is the Woo/Spelke branch: the comparator's load-bearing features are likely motion-contingency / goal-directedness, which V3 substrate cannot deliver without genuine other-agents. Route MECH-095 from `substrate_ceiling` (V3-tractable) to `substrate_conditional` with V4 dependency on V4-1 multi-agent ecology. SD-047 retired or kept as ancillary substrate enrichment. |
| Flat curve, all arms PASS | All-PASS | **Substrate-ceiling diagnosis was wrong but in the opposite direction.** Investigate whether V3-EXQ-506 had a non-substrate confound (training pathology, seed pathology, etc.). |

This is a falsifiable substrate test in the strong sense: each row of
the interpretation grid maps a distinct experimental signature to a
distinct architectural conclusion, including a clean route from
falsification to a different SD candidate (V4-1 multi-agent ecology).
The Woo/Spelke branch is not a graceful loss — it is a productive
finding that reroutes substrate work to V4.

**Lit-pull provenance:** the entries supporting this revised protocol
are in `evidence/literature/targeted_review_sd_047/`:
Asai 2016 (load-bearing, supports conf=0.83), Sawtell 2010 (mechanism
grounding, supports 0.80), Pitcher & Ungerleider 2021 (pathway
specialisation, supports 0.78), Davidson & Wolpert 2005 (forward-model
scaffold, supports 0.70), Woo/Liu/Spelke 2023 (falsifier, weakens 0.65).
SD-047 lit_conf was 0.0 before this pull and is 0.796 after.

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
