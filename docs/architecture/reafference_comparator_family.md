# Reafference Comparator Family

> **Claim:** ARC-061 (`self_attribution.reafference_comparator_family`,
> candidate). This document is the design-doc backing for that claim.
>
> Describes the structural relationship between three substrate-level
> implementations of the same reafference-cancellation motif in REE V3.
> The individual constituent claims (MECH-095, ARC-058, MECH-094) are
> registered separately; ARC-061 captures their shared architecture.
>
> Last updated: 2026-05-03

---

## The core motif

Von Holst's reafference principle (1950) names a specific computational
problem: a self-monitoring agent must distinguish signals produced by its
own actions (reafference) from signals produced by the world acting on
it (exafference). The solution is a forward model that predicts the
expected self-caused signal; the comparator cancels it; what remains is
the world's contribution. Without this, every self-generated movement
is experienced as externally imposed, and every external event is either
attributed to self or lost in the noise of action.

This problem does not resolve once at the level of motor commands and
stop. It recurs at every level of representational abstraction at which
a self-monitoring system operates:

- **Motor/action level**: did this body change result from my motor command
  or from the environment?
- **Interoceptive level**: did this affective/somatic state change result from
  my own internal dynamics or from an external aversive input?
- **Propositional level**: did this thought/belief originate from my own
  generative process or from something injected from outside?

The same motif answers all three:

```
Forward model F: given current state + agent's action, predict expected signal
Comparator C:    observed signal - F(state, action) = residual
Authorship tag T: if |residual| < threshold -> self-generated
                  if |residual| > threshold -> other-generated
```

In REE V3, each level is implemented with its own substrate, its own
threshold calibration, and its own failure modes — but the architectural
pattern is identical.

---

## Three instantiations

### Level 1 — Motor / action comparator

**Claim:** MECH-095 (`tpj.agency_detection_comparator`, status: active,
`epistemic_category: substrate_ceiling`)

**What it computes:** `E2_harm_s(z, a_actual) - E2_harm_s(z, a_cf)` — the
counterfactual gap on the harm forward model. Self-caused state change has
a distinctive causal signature; environmental change does not. The comparator
licenses the authorship tag when that gap exceeds threshold.

**REE substrate:** `E2_harm_s` (ARC-033 independent-per-stream path, or
ARC-058 shared-trunk variant). The counterfactual branch is the SD-003/SD-029
pipeline.

**Biological analogue:** Cerebellum (efference-copy cancellation of
motor-induced somatosensory change — Blakemore/Frith 2000); SMA/TPJ
network for social agency attribution (Pitcher & Ungerleider 2021, third
visual pathway / STS for dynamic social perception).

**Failure mode (clinical):** Schneiderian first-rank passivity phenomena.
Shallow comparator slope across S/N → symmetric over-attribution (agent
claims responsibility for environmental changes) AND under-attribution
(agent fails to register own causal footprint). Same mechanism, opposite
error directions depending on noise regime (Asai 2016).

**V3 status:** `substrate_ceiling` — CausalGridWorldV3's "other-caused"
change is too thin (single scheduled hazard source) for the comparator to
produce a legible signal. V3-EXQ-506 confirmed the ceiling signature
(C4-only-PASS, r2_s_to_a ~ 0.99 invariant to action type). **SD-047
substrate now IMPLEMENTED 2026-05-03** (calibration ratio 1.95:1 within
1:1-2:1 target band; bit-identical OFF verified; 4-arm sweep validation
queued as V3-EXQ-509/510).

**Unblocking SD:** SD-047 (`environment.multi_source_dynamics`, **IMPLEMENTED
2026-05-03**). Design doc: `docs/architecture/sd_047_multi_source_dynamics.md`.

---

### Level 2 — Interoceptive / affective comparator

**Claim:** ARC-058 (`harm_stream.shared_forward_trunk`, status: candidate,
v3_pending; competes with ARC-033)

**What it computes:** Modality-independent unsigned aversive prediction
error from a shared `HarmForwardTrunk`, with stream-specific heads reading
out signed per-modality residuals (`z_harm_s` somatic, `z_harm_a`
affective). The interoceptive comparator tags whether a somatic/affective
state change is predicted by current body state and ongoing dynamics
(self-generated: injury, drive depletion, pain progression) or anomalous
(other-generated: unexpected assault, unpredicted aversive).

**REE substrate:** ARC-058 `HarmForwardTrunk` (shared-substrate hypothesis)
or ARC-033 independent-per-stream paths (competing). The relevant
authorship-tag output feeds `z_harm_a` stream and modulates drive state
attribution.

**Biological analogue:** Anterior insular cortex (Craig 2009 interoceptive-
salience hub); Seth & Friston 2016 active interoceptive inference framework
(predictive processing of visceral states with free-energy-minimising
body-state regulation). Failure mode: affective prediction errors attributed
to external sources when the interoceptive comparator under-predicts
self-generated affective change (FND, conversion disorder — Lyndon 2026;
negative-symptom self-other indistinctness — Jeganathan & Breakspear 2021).

**Failure mode (clinical):** Somatic / affective passivity — "made feelings",
made emotions, somatic passivity experiences. The interoceptive stream
cannot tag its own affective changes as self-generated; they are
experienced as externally imposed.

**V3 status:** V3-tractable in principle (SD-011 dual-stream substrate
is IMPLEMENTED; `z_harm_a` pathway active). The comparator itself is
not yet a discrete mechanism — ARC-058 is the architectural claim that
would register it, and is currently competing with ARC-033. V3-EXQ-508
(body-damage ablation) weakened ARC-033 at its borderline boundary,
which is evidence in favour of the ARC-058 shared-trunk path.

**Gap:** No SD claim registered for the interoceptive-comparator substrate
enrichment (analogous to SD-047 for Level 1). The Level 2 comparator
needs its own substrate-noise calibration: stochastic perturbation of
the body-damage stream (interoceptive noise) to probe the same inverted-U
calibration curve. This is a pending work item — see section below.

---

### Level 3 — Propositional / simulation tag

**Claim:** MECH-094 (`default_mode.simulation_real_distinction_write_profile`,
status: stable, confirmed_established)

**What it computes:** A categorical write-gate φ(z) that marks simulation-mode
content with `hypothesis_tag = True`, preventing it from accumulating in
the viability residue field as committed experience. Real-experience content
carries `hypothesis_tag = False` and writes normally. The gate is the
authorship tag for propositional/simulation content.

**REE substrate:** `hypothesis_tag` boolean threaded through
`HippocampalModule.replay()`, `tick()` simulation paths, and SD-032e
`pACC` autonomic controller. Tested directly in V3-EXQ-499 (forced-
injection discriminative pair: ARM_A with tag active suppresses 50 drive-
bias accumulation events, ARM_B without tag accumulates normally).

**Biological analogue:** PFC/mPFC source monitoring (Corlett 2025 aberrant-
salience framework); ACC-hypothesis-tag function (MECH-094 notes); pretend-
play tag co-exercise with ARC-049 (MECH-198/199/200/201 maturational
cluster). Tag loss = confabulation (MECH-094 primary) and psychosis-
adjacent states (MECH-201 notes). Distinct from MECH-095 action-passivity
by being content-proximal rather than action-proximal.

**Failure mode (clinical):** Thought insertion/withdrawal (internally
generated thought lacking hypothesis tag, experienced as external);
confabulation (replay content writes as real experience). Mechanistically
distinct from action-passivity (Level 1) and affective passivity (Level 2).

**V3 status:** Stable, confirmed_established. No substrate gap — MECH-094
is the most mature member of the family in V3.

---

## Shared diagnostic principles

These principles apply to all three levels. They derive from the common
architectural substrate (noise-dependent forward-model comparator) rather
than from any level-specific implementation:

### 1. Symmetric over/under-attribution as calibration indicator

A comparator with a shallow slope produces both over-attribution (agent
claims credit for external change) and under-attribution (agent misses own
causal footprint) across S/N regimes — not just one direction. The symmetric
error pattern is the diagnostic fingerprint of calibration failure, not of
a unidirectional bias.

Asai (2016, Psychiatry Research): agency-rating slope is a continuous
function of S/N. Schizotypal participants show shallower slopes that
produce both error types symmetrically across contexts.

**Implication for REE monitoring:** an agent whose Level 1 or Level 2
comparator shows systematic error in only one direction probably has a
floor or ceiling problem; symmetric errors across conditions indicate a
slope (calibration) problem.

### 2. Non-monotonic noise-dependence (stochastic resonance)

Comparator competence has an optimal substrate-noise level, not a
maximum-tolerance level. Too little environmental noise leaves the
comparator with no signal to detect; too much noise overwhelms the
comparison. An intermediate noise level is the calibration optimum.

Ward et al. (2010, PLoS ONE): 40 Hz transient response in bilateral
auditory cortex is enhanced — not degraded — by added broadband noise
at an intermediate level. Synchronization between cortical regions shows
the same inverted-U.

**Implication for SD-047 validation:** the 4-arm noise-level sweep
(OFF / 0.25x / 1.0x / 4.0x) probes this curve directly. The same
sweep protocol should be used for Level 2 calibration when its SD
is implemented.

### 3. Single substrate pathology → bidirectional surface consequences

One substrate-level problem (E/I imbalance, precision miscalibration)
produces multiple surface failure modes in opposite directions, because
the comparator has multiple consumers that each exhibit the imbalance
differently.

Jardri & Deneve (2013, Brain): circular belief propagation from E/I
imbalance produces hallucinations AND paradoxical immunity to perceptual
illusions from the same mechanism.

Nassar et al. (2021, PNAS): all-or-nothing belief updating produces
both over-sensitivity (in volatile environments) and under-sensitivity
(in stable environments) from the same computational pathology.

**Implication for taxonomy:** when an agent shows contradictory
attribution errors across contexts, the first diagnostic hypothesis
should be a single substrate-calibration problem, not two independent
faults.

### 4. Substrate enrichment precedes content-level intervention

Because the failure is at the substrate-calibration level (comparator
slope), it cannot be corrected by content-level interventions (changing
what the agent believes, editing priors). SD-047 must land before
MECH-095 can be honestly tested — not because the claim is wrong, but
because the substrate is too thin to generate the needed signal.

**Implication for clinical analogy:** substrate-calibration interventions
(pharmacological, environmental richness) should improve comparator
function before content-level CBT addresses the resulting beliefs (P-018
in psychiatric_predictions.md).

---

## Cross-level summary

| | Level 1 (motor/action) | Level 2 (interoceptive) | Level 3 (propositional) |
|---|---|---|---|
| **Claim** | MECH-095 | ARC-058 | MECH-094 |
| **Subject** | tpj.agency_detection_comparator | harm_stream.shared_forward_trunk | simulation_real_distinction |
| **REE substrate** | E2_harm_s counterfactual gap | HarmForwardTrunk + z_harm_a | hypothesis_tag write gate |
| **Timescale** | ms -- seconds | seconds -- minutes | episode |
| **Modality** | sensorimotor | somatic/visceral | conceptual/propositional |
| **Biological** | cerebellum/SMA/TPJ | insula/AIC | PFC/ACC/mPFC |
| **Failure mode (clinical)** | passivity of action, made impulses | made feelings, somatic passivity | thought insertion, confabulation |
| **Failure direction** | symmetric over/under per S/N regime | symmetric over/under per noise | tag loss -> real attribution of simulation |
| **Authorship tag** | cf_gap > threshold | affective-PE > threshold | hypothesis_tag = True/False |
| **V3 status** | substrate_ceiling, SD-047 IMPLEMENTED | V3-tractable, SD-048 pending | stable, confirmed_established |
| **Calibration SD** | SD-047 (implemented 2026-05-03) | SD-048 (ready) | not applicable |
| **Key literature** | Asai 2016, Blakemore/Frith 2000 | Seth/Friston 2016, Lyndon 2026 | Corlett 2025, MECH-094 notes |

---

## Implementation gaps

### Gap 1: Level 2 substrate enrichment SD (highest priority)

Level 2 has no SD claim. The interoceptive comparator's substrate-calibration
test requires controlled perturbation of the body-damage / affective stream —
an interoceptive analog of SD-047's multi-source noise sweep. Concretely:
stochastic variation in `z_harm_a` background amplitude, independent of
the agent's actions, at calibrated intensity. This exposes whether the
Level 2 comparator can separate agent-caused affective change from
environmental-origin affective perturbation.

Suggested claim: `SD-NNN` (`body.interoceptive_noise_dynamics`), depending
on SD-022 (body-damage substrate, IMPLEMENTED) and SD-011 (dual
nociceptive streams, IMPLEMENTED). V3-tractable.

### Gap 2: Cross-level interaction

V3 can probe each level independently but cannot test whether a failure
at one level propagates to another. In biological systems, action-passivity
and thought insertion co-occur in schizophrenia — suggesting either shared
substrate or cross-level dependency. The question of whether Level 1
calibration failure induces Level 3 tag instability (or vice versa) cannot
be answered with independent single-level probes.

This is V4-1 territory (multi-agent ecology + full simultaneous activation
of all three comparator levels). See `docs/architecture/v4_spec.md`.

### Gap 3: Cross-level interaction experiment

Level 1 (SD-047) and Level 2 (SD-048) are independently implementable
and will be validated separately. Once both land, a joint experiment
probing the cross-level interaction becomes the next step: does Level 1
miscalibration propagate to Level 2 tag instability, or are the levels
cleanly decoupled? That question cannot be answered with single-level
probes. Deferred pending both SDs validated.

---

## V4 implications

When genuine other-agents are present (V4-1), all three comparator levels
activate simultaneously and interact:

- Level 1 must discriminate self-caused from agent-caused from environment-caused
  change (three-way, not two-way attribution)
- Level 2 must attribute affective contagion (other-agent's distress state
  producing prediction error in own interoceptive stream) as other-generated
- Level 3 must maintain the simulation/real tag for internally generated
  models of other agents' states (theory-of-mind simulations carry
  hypothesis_tag = True)

The shared diagnostic principles (symmetric over/under-attribution,
non-monotonic noise-dependence, single substrate -> bidirectional surface)
all generalise to the multi-agent case. In particular, a Level 2 calibration
failure in the presence of other-agents produces affective contagion
indistinguishable from own affective experience — a computational model of
the empathy dysregulation cluster in borderline/dissociative presentations.

That claim cohort is currently V4-bound. The V3 work (SD-047 for Level 1,
SD-048 (Level 2 interoceptive noise dynamics)) lays the calibration
infrastructure that V4 social probes will need.

---

## Related documents

- `docs/architecture/sd_047_multi_source_dynamics.md` — SD-047 specification
  (Level 1 substrate enrichment)
- `docs/architecture/substrate_roadmap.md` — V3 enrichment planning
- `docs/architecture/v4_spec.md` — V4 multi-agent ecology scope
- `docs/architecture/control_plane.md` — hypothesis_tag threading
  (MECH-094 Level 3 implementation)
- `REE_assembly/evidence/literature/targeted_review_connectome_mech_095/` —
  15 entries grounding Level 1 substrate-ceiling diagnosis
- `REE_assembly/evidence/literature/targeted_review_arc_058/` —
  Level 2 interoceptive-comparator literature
- `ai-cognitive-failure-taxonomy/failure_modes/agency_attribution_failure.md` —
  taxonomy entry anchored on Level 1 failure (Asai 2016)
- `ai-cognitive-failure-taxonomy/docs/psychiatric_predictions.md` —
  P-017 / P-018 covering comparator-slope predictions
