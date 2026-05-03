# SD-048: Interoceptive Noise Dynamics

**Claim ID:** SD-048
**Subject:** `body.interoceptive_noise_dynamics`
**Status:** IMPLEMENTED 2026-05-03 (substrate; v3_pending until validation experiment lands)
**Registered:** 2026-05-03
**Depends on:** SD-011 (dual nociceptive streams, IMPLEMENTED),
SD-022 (directional limb damage, IMPLEMENTED)
**Design doc for:** Level 2 of the reafference comparator family
(see `docs/architecture/reafference_comparator_family.md`)
**Implementation:** `ree-v3/ree_core/environment/causal_grid_world.py`
(CausalGridWorldV2 flat `__init__` kwargs; readout-side perturbation on
`harm_obs_a` in `_get_observation_dict` via `_apply_interoceptive_noise`).
See `ree-v3/CLAUDE.md` SD-048 entry for the full implementation note,
config defaults, activation-smoke results, and implementation-choice
deviations from this doc.

---

## Problem

SD-022 gave `z_harm_a` an agent-caused source: limb damage accumulates
when the agent moves through hazards and heals slowly. That was the
necessary first step — without it, `z_harm_a` had no agent-caused
variance at all (the r2_s_to_a = 0.996 failure documented in SD-022's
functional_restatement).

But the Level 2 comparator problem is the mirror image of the Level 1
problem (MECH-095 / SD-047): the comparator must separate agent-caused
body-state change from body-state change that arises independently of
what the agent does. After SD-022, all `z_harm_a` variance is either
agent-caused (limb damage from hazard contact) or deterministic
(heal_rate = 0.002/step). There is no independent body-state background
for the comparator to calibrate against.

The Level 2 claim (ARC-058, HarmForwardTrunk) asserts that the
interoceptive forward model can encode an unsigned aversive prediction
error shared across body-state sources. That claim is untestable on
current substrate: when all interoceptive variance is agent-caused, a
trivial forward model `E2_harm_a(z, a) = z_harm_a_next` passes by
memorising the agent's action-damage coupling, not by learning to
separate self-caused from body-noise-caused change.

SD-048 adds three concurrent stochastic body-state perturbation sources
that are NOT caused by the agent's motor output. With these active, the
interoceptive comparator must learn to distinguish:

- Agent-caused: `I moved N through a hazard -> limb N is more damaged -> z_harm_a increased`
- Body-generated: `autonomic fluctuation / sensitisation spike / fatigue drift -> z_harm_a increased despite no new hazard contact`

This is the Level 2 reafference-cancellation problem in its minimal
honest form.

---

## Mechanism

SD-048 adds three concurrent stochastic body-state noise sources, each
operating at a distinct temporal scale and statistical character. The
design mirrors SD-047's three environmental sources: the comparator must
learn structural self/body-noise signatures, not just filter a single
noise pattern.

### Source 1: Autonomic background fluctuation

Fast, continuous, low-amplitude additive noise on `harm_obs_a` at
every step.

- **Biological analog:** beat-to-beat heart rate variability, spontaneous
  sympathetic fluctuations, background nociceptive sensitisation, the
  irreducible noise floor of the insular interoceptive map.
- **Statistical character:** i.i.d. Gaussian at the step level (no
  inter-step autocorrelation). Amplitude small relative to agent-caused
  limb-damage variance.
- **Parameters:** `autonomic_noise_scale` (default 0.02 normalised
  harm units), applied per step to `harm_obs_a` directly.
- **Temporal scale:** fast (every step).

### Source 2: Sensitisation spikes (transient amplification events)

Discrete Poisson-distributed events that transiently amplify `harm_obs_a`
by a multiplicative factor, then decay exponentially.

- **Biological analog:** inflammatory sensitisation flares, allodynic
  episodes, spontaneous visceral pain amplification, central sensitisation
  bursts. These are not caused by new tissue damage — they are changes in
  the gain of the interoceptive reporting pathway.
- **Statistical character:** Poisson onset (rate `sensitisation_rate`,
  default ~0.008/step), multiplicative amplitude (`sensitisation_magnitude`,
  default 1.8x), exponential decay with half-life `sensitisation_halflife`
  (default 15 steps). Multiple events can overlap (additive amplification).
- **Parameters:** `sensitisation_rate`, `sensitisation_magnitude`,
  `sensitisation_halflife`.
- **Temporal scale:** medium (onset discrete, decay ~15-30 steps).

### Source 3: Fatigue drift

Slow AR(1) accumulation in a latent background fatigue state that adds
to `harm_obs_a` continuously.

- **Biological analog:** metabolic fatigue, allostatic load accumulation,
  sleep pressure, prolonged sympathetic activation. Fatigue is not the
  same as tissue damage — it is a slowly-rising body-state cost that
  persists independently of what the agent is currently doing.
- **Statistical character:** AR(1) process with coefficient
  `fatigue_ar_coeff` (default 0.995, very slow decay), driven by
  low-amplitude Gaussian innovations. Contribution to `harm_obs_a` is
  additive and proportional to current fatigue state.
- **Parameters:** `fatigue_ar_coeff`, `fatigue_noise_scale` (default
  0.005/step).
- **Temporal scale:** slow (episode-length drift, resets at episode end).

### Why three sources?

Same logic as SD-047. A single noise source can be filtered by matching
its specific statistical signature. Three sources with qualitatively
different characters (fast i.i.d. / discrete transient / slow drift)
force the comparator to learn a structural signature of agent-causation
rather than a specific noise pattern. The sources correspond to three
biological timescales:

- Autonomic (seconds) → step-level jitter
- Inflammatory/sensitisation (minutes) → episode-phase transient
- Metabolic/allostatic (hours) → full-episode drift

### Calibration target

1:1 to 2:1 body-noise-caused harm-state-change events to agent-caused
harm-state-change events per episode, at default calibration (ARM_2).

This mirrors SD-047's 1:1-2:1 calibration target. The goal is that the
background noise is large enough to be non-trivial for the comparator
but not so large that agent-caused signal is drowned. Events are defined
as steps where `|delta_harm_obs_a| > threshold_minor` — both agent-caused
(hazard contact) and body-noise-caused (sensitisation spike, fatigue
step) count.

---

## Child mechanisms (deferred)

These sub-mechanisms will register when the SD implements and when their
distinct functional signatures become measurable:

### MECH-(TBD): Autonomic-noise interoceptive self-attribution class

The fast Gaussian source contributes a continuous `self/body-noise`
calibration signal to the comparator. Whether ARC-058's trunk represents
the autonomic noise floor as a distinct unsigned-PE class (separate from
sensitisation and fatigue) is an empirical question.

### MECH-(TBD): Sensitisation-event interoceptive self-attribution class

The discrete Poisson source tests whether the comparator can tag
sensitisation-origin harm-obs changes as non-agent-caused. Failure
produces "made feelings" phenomenology (body changes attributed to
external agency). The sensitisation profile — transient, large amplitude,
multiplicative — is structurally distinct from the fatigue profile.

### MECH-(TBD): Fatigue-drift interoceptive trajectory class

The slow AR(1) source tests whether the comparator represents fatigue
as a self-generated body trajectory (expected given prior fatigue state)
or misattributes late-episode fatigue accumulation to environmental harm.

Register these as MECH claims when SD-048 is implemented and the
validation experiment runs.

---

## Architecture context

SD-048 sits at the **body-state substrate** layer, parallel to SD-022
(which added agent-caused body-state variance) and SD-011 (which split
the harm stream into `z_harm_s` and `z_harm_a`). SD-048 adds the
other-caused side of the `z_harm_a` variance that SD-022 did not address.

Relationship to SD-047: the two SDs address the same general problem
(substrate too thin for comparator calibration) at different levels:

- SD-047: external environment → Level 1 motor/action comparator (MECH-095)
- SD-048: internal body state → Level 2 interoceptive comparator (ARC-058)

They are independently implementable and can run simultaneously. An
experiment with both enabled would test the interaction: does a richer
body-state background affect the Level 1 comparator, or are the two
levels cleanly decoupled? That cross-level question is not the primary
target of either SD individually.

Relationship to ARC-058 vs ARC-033 arbitration: SD-048 is necessary for
both paths. Whether the interoceptive comparator uses a shared trunk
(ARC-058) or independent per-stream models (ARC-033) is an architectural
question that SD-048 does not settle — but neither can be honestly tested
until the substrate has independent body-state variance to discriminate.

---

## What this SD enables

- **ARC-058** (`harm_stream.shared_forward_trunk`, primary) — the
  HarmForwardTrunk claim can now be tested at substrate level. C1-C3
  criteria analogous to MECH-095 (body-noise-event selectivity,
  self-vs-body-noise gap, interoceptive attributor calibration) become
  measurable. ARC-058 moves from V3-tractable/no-substrate to
  directly testable.
- **ARC-033** (competing claim) — same substrate enrichment benefits
  independent-per-stream comparator testing. The arbitration between
  ARC-033 and ARC-058 is best run on SD-048-enriched substrate where
  both can express their architectural signatures.
- **ARC-061** (`self_attribution.reafference_comparator_family`) —
  Level 2 contribution. ARC-061 cannot promote until Level 2 has
  experimental support; SD-048 is the prerequisite.
- **SD-011 sub-claims** — several z_harm_a dynamics claims become
  testable with non-trivial body-state variance.
- Possibly **MECH-112** (wanting/liking dissociation) if fatigue drift
  interacts differentially with the wanting vs liking gradient fields.

---

## Validation experiment (deferred)

**Pre-registered protocol for SD-048 validation — noise-level sweep:**

The same architectural logic that motivated SD-047's 4-arm noise sweep
applies here (Asai 2016 non-monotonic comparator competence; Ward 2010
stochastic resonance in human interoceptive EEG). Binary ON/OFF is
ambiguous between "SD-048 works" and "SD-048 overshot calibration."

**Primary metric:** ARC-058 (or ARC-033 as baseline) `z_harm_a`
comparator performance:

- **C1:** Body-noise-event selectivity — comparator output discriminates
  body-noise-caused `z_harm_a` spikes from agent-caused spikes
  (AUC or ROC above chance).
- **C2:** Self-vs-body-noise gap — forward model residual is larger for
  body-noise events than for agent-caused events in matched-amplitude
  conditions.
- **C3:** Interoceptive attributor calibration — comparator output
  correlates with actual event origin (agent-caused vs body-noise-caused)
  across conditions.
- **C4:** Base `z_harm_a` forward model accuracy (r2) — must remain
  high in OFF arm (sanity check that SD-048 doesn't degrade base model
  when disabled).

**Arms:**

- **ARM_0 (OFF baseline):** `interoceptive_noise_enabled=False`. SD-022
  only. Should reproduce current substrate ceiling: C1-C3 fail or are
  untestable (no body-noise events exist), C4 holds.
- **ARM_1 (0.25x):** All three sources at 25% of default scale.
  Below-calibration prediction: C1-C3 may show modest signal but comparator
  competence is impaired by insufficient background variance.
- **ARM_2 (1.0x default):** All sources at default calibration. Predicted
  C1-C3 PASS. This is the hypothesised optimum from the Ward/Asai
  non-monotonicity principle.
- **ARM_3 (4.0x):** All sources at 4x scale. Above-calibration prediction:
  body noise drowns agent-caused signal, comparator competence degrades
  (C1-C3 drift back toward FAIL).

**Interpretation grid:**

| ARM_2 (default) | ARM_0 (OFF) | Interpretation |
|---|---|---|
| C1, C2, C3 PASS | C1, C2, C3 FAIL | **SD-048 validated.** Route ARC-058 to standard testable; move Level 2 from pending to evaluable in ARC-061. |
| Inverted-U with ARM_2 peak | Same as above | **SD-048 validated with calibration confirmation.** Non-monotonicity directly observed. |
| ARM_1 or ARM_3 peaks instead of ARM_2 | C1-C3 FAIL | **SD-048 validated, calibration off.** Recalibrate per-source scales; architectural conclusions hold. |
| Flat curve, all arms FAIL | C1-C3 FAIL | **Falsification of V3-tractable assumption.** The interoceptive comparator's load-bearing features require a richer body-state substrate (temperature, proprioception, nausea, visceral specificity) that CausalGridWorldV3 cannot provide. Route ARC-058 from V3-tractable to `substrate_conditional` with dependency on a richer body-state substrate. SD-048 retired or kept as ancillary enrichment for SD-011 downstream claims. |
| ARM_2 PASS, ARM_0 also PASS | (trivial comparator) | **SD-048 irrelevant.** Comparator passes without noise, so it was never substrate-gated — revisit C1/C2/C3 threshold calibration and confirm they are non-trivial. |

---

## Implementation surface

```python
# New config fields in REEConfig (ree_core/config.py)
interoceptive_noise_enabled: bool = False           # master switch
interoceptive_noise_scale: float = 1.0              # global multiplier (the arm sweep lever)

# Source 1: autonomic background
autonomic_noise_scale: float = 0.02                 # per-step Gaussian SD (normalised harm units)
autonomic_noise_enabled: bool = True                # per-source ablation switch

# Source 2: sensitisation spikes
sensitisation_rate: float = 0.008                   # Poisson events per step
sensitisation_magnitude: float = 1.8               # multiplicative amplifier
sensitisation_halflife: int = 15                    # steps to half-amplitude decay
sensitisation_enabled: bool = True

# Source 3: fatigue drift
fatigue_ar_coeff: float = 0.995                     # AR(1) persistence
fatigue_noise_scale: float = 0.005                  # per-step innovation SD
fatigue_contribution_weight: float = 0.15           # weight on harm_obs_a additive sum
fatigue_enabled: bool = True
```

**Bit-identical OFF requirement:** when `interoceptive_noise_enabled=False`,
the body-state update path must be identical to pre-SD-048 baseline
(no RNG draws, no state variables). All three sources must also be
individually disableable (`autonomic_noise_enabled`, etc.) for ablation
experiments.

**Location:** `ree_core/environments/causal_grid_world.py`, body-state
update section (analogous to SD-022's limb_damage accumulation block).
New internal state variables: `_fatigue_state: float` (reset to 0.0 at
episode start), `_sensitisation_state: float` (active amplification).

**Episode reset:** `_fatigue_state` and `_sensitisation_state` reset to
0.0 at `reset()`. Sensitisation events are i.i.d. per episode.

---

## Related claims

- **ARC-058** — primary target. SD-048 is the substrate condition for
  honest ARC-058 testing.
- **ARC-033** — competing claim. Benefits from same substrate enrichment;
  arbitration runs on SD-048-enabled substrate.
- **ARC-061** — Level 2 contribution to the reafference comparator
  family. See `docs/architecture/reafference_comparator_family.md`.
- **SD-011** — prerequisite. The `z_harm_a` stream must exist before
  its interoceptive noise dynamics can be added.
- **SD-022** — prerequisite. Agent-caused body-state variance must
  exist before other-caused noise is meaningful as a calibration
  background.
- **SD-047** — Level 1 counterpart. Same architectural logic at the
  environmental layer. Independently implementable; can run in
  parallel. Cross-level interaction (joint SD-047 + SD-048) deferred
  to a later experiment.
