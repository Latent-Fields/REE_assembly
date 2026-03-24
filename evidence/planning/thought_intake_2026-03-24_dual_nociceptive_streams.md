# Thought Intake: Dual Nociceptive Stream Architecture

**Date:** 2026-03-24
**Session type:** Architectural reasoning from experimental evidence + literature synthesis
**Trigger:** EXQ-093/094 FAILs — both experiments confirmed bridge_r2=0 (z_world perp z_harm), making the SD-003 HarmBridge counterfactual pipeline architecturally infeasible
**Output:** SD-011 registered (dual nociceptive stream), ARC-033 registered (harm forward model), implementation begun in ree-v3

---

## Problem That Triggered This

EXQ-093 fixed the E3 head training bug but bridge_r2=0.0 persisted.
EXQ-094 confirmed: training E3 on HarmBridge(z_world) outputs regressed 100x vs EXQ-088.

SD-003 counterfactual as designed requires:
```
z_harm_cf = HarmEncoder(E2.world_forward(z_world, a_cf))
```
This bridges from z_world to z_harm. SD-010 makes this impossible by architectural design: z_world and z_harm are orthogonal independent streams. The bridge has nothing to learn.

The question raised: is there a way to make z_harm counterfactually predictable without a cross-stream bridge?

---

## The Neuroscience Grounds: Two Nociceptive Pathways in Humans

The human nociceptive system separates into two anatomically and functionally distinct ascending pathways:

### Stream 1: Sensory-Discriminative (Lateral, Aδ-fiber, Fast)
- **Fiber type:** Aδ (myelinated, 20-30 m/s)
- **Spinal pathway:** Neospinothalamic tract — direct, few synapses
- **Thalamic relay:** VPL nucleus (somatotopic, point-to-point)
- **Cortical targets:** S1 (primary somatosensory, localization) → S2 (intensity discrimination)
- **Encodes:** WHERE is the noxious stimulus, HOW SHARP/INTENSE, precise location
- **Temporal profile:** Immediate on/off; tracks stimulus with minimal lag
- **Key property:** **Predictable from action** — moving away from a hazard immediately reduces proximity signal. The brain generates forward model predictions of this stream; predictability suppresses sensory-discriminative activity (reafference cancellation applies here)
- **Functional role in REE:** Proximity/intensity encoding; provides the signal that a harm forward model E2_harm_s can learn to predict

### Stream 2: Affective-Motivational (Medial, C-fiber, Slow)
- **Fiber type:** C fibers (unmyelinated, 0.5-2.0 m/s)
- **Spinal pathway:** Paleospinothalamic tract — multisynaptic via brainstem reticular formation
- **Thalamic relay:** Intralaminar nuclei (CM, PF) — no fine somatotopy; large receptive fields
- **Cortical targets:** ACC (unpleasantness/escape motivation) → anterior insula (homeostatic integration) → amygdala (aversion learning + autonomic response)
- **Encodes:** HOW BAD is this for the body, accumulated homeostatic deviation, unpleasantness/urgency
- **Temporal profile:** Slower to change; cumulative; integrates mood, prior threat, body state
- **Key property:** **NOT directly predictable from single action** — depends on accumulated homeostatic context, learned threat value, autonomic state. Less suppressed by predictability; more driven by homeostatic inference ("will I recover?")
- **Functional role in REE:** Sustained motivational/urgency signal into E3; ARC-016 harm variance gating; does NOT need a forward model

### Melzack & Casey (1968) three-component model

The foundational framing is Melzack & Casey's 1968 three-component model:
1. **Sensory-discriminative** — intensity, location, quality, duration (lateral pathway → S1/S2)
2. **Affective-motivational** — suffering, urgency to escape (medial pathway → ACC/insula/amygdala)
3. **Cognitive-evaluative** — appraisal, context, meaning (prefrontal modulation of both)

Craig (2002, 2003, 2009) unified this under interoception: pain is a homeostatic emotion, one of a family (also temperature, hunger, thirst, respiratory drive) that signal homeostatic deviation. The insular cortex (posterior: primary homeostatic body map; anterior: affective integration) is the key convergence zone.

### Key dissociation evidence

Rainville et al. (1997, Science): hypnotic modulation of pain *unpleasantness* activates ACC but NOT S1. Modulation of pain *intensity* affects S1. This is the gold-standard dissociation confirming the two streams encode genuinely different properties.

Predictability studies: Keltner et al. (2006, J Neurosci) — predictable pain suppresses sensory cortex activity (forward model cancellation), while affective response is less suppressed.

---

## Architectural Implication for REE

The EXQ-093/094 failure is not a bug in the bridge — it is a correct outcome. z_world ⊥ z_harm by SD-010 design, so bridging from z_world to z_harm was always infeasible. The fix is to decompose z_harm into the two functional streams it conflates:

### z_harm_s (sensory-discriminative, Aδ-pathway analog)
- Input: `harm_obs_s` = immediate hazard/resource proximity vector (what the current `harm_obs` is)
- Encoder: `HarmEncoderS(harm_obs_s → z_harm_s)` — the current HarmEncoder
- **Key addition:** A harm forward model `E2_harm_s(z_harm_s, action) → z_harm_s_next`
  - This is tractable: proximity decreases predictably when agent moves away from hazard
  - Structure is analogous to `E2.world_forward(z_world, action) → z_world_next`
- SD-003 counterfactual becomes: `z_harm_s_cf = E2_harm_s(z_harm_s, a_cf)`
  - `causal_sig = E3(z_harm_s_actual) - E3(z_harm_s_cf)`
  - No cross-stream bridge needed — attribution operates entirely within the harm stream

### z_harm_a (affective-motivational, C-fiber/paleospinothalamic analog)
- Input: `harm_obs_a` = accumulated/integrated harm exposure signal
  - In CausalGridWorldV2: EMA of harm_obs_s over recent history, or sum of proximity × duration
  - Represents sustained body threat, not momentary proximity
- Encoder: `HarmEncoderA(harm_obs_a → z_harm_a)`
- **NOT counterfactually modeled** — no forward model needed for this stream
- Role: sustained urgency/motivational signal into E3
  - ARC-016 harm variance gating: variance in z_harm_a across danger levels tests whether E3 commit threshold is modulated by accumulated threat state
  - EXQ-094 regression (harm_var → 5e-7) was because E3 trained on bridge noise; with z_harm_a carrying genuine accumulated signal, ARC-016 becomes testable

### SD-003 redesign

The validated SD-003 pipeline (EXQ-030b, world_forward_r2=0.947) operates on z_world:
```
z_world_cf = E2.world_forward(z_world, a_cf)
causal_sig = E3(z_world_actual) - E3(z_world_cf)
```
This is valid for world-stream attribution but insufficient now that E3 operates on z_harm, not z_world.

The redesigned SD-003 pipeline (post-SD-011):
```
z_harm_s_cf = E2_harm_s(z_harm_s, a_cf)
causal_sig = E3_harm(z_harm_s_actual) - E3_harm(z_harm_s_cf)
```
The EXQ-030b validation remains valid as a **proof-of-concept for the counterfactual pipeline architecture** — it shows the E2 forward model achieves R²=0.947 and the counterfactual delta correctly tracks causal structure. The same architecture now needs to be applied to z_harm_s specifically.

---

## What's New vs. Existing REE Docs

| Topic | Status |
|-------|--------|
| ARC-027: harm stream as parallel thalamic pathway | Already registered (active) |
| SD-010: harm_obs → HarmEncoder → z_harm separate from z_world | Already implemented |
| ARC-027 notes LeDoux "low road" (amygdala bypass) | Covered in notes |
| **Dual nociceptive streams (discriminative vs. affective)** | **NEW — SD-011** |
| **Sensory-discriminative stream is forward-predictable from action** | **NEW — ARC-033** |
| **Affective stream as accumulated homeostatic deviation** | **NEW — part of SD-011** |
| **SD-003 redesign using z_harm_s forward model** | **NEW — SD-003 note update** |
| Melzack/Casey three-component model | Referenced in ARC-027 notes but not formalized |
| Craig interoception/insular cortex homeostatic map | **NEW literature grounding** |
| ACC encodes unpleasantness, S1 encodes intensity (Rainville 1997) | **NEW literature grounding** |

---

## New Claims Proposed

### SD-011: Dual nociceptive stream separation
The harm stream separates into:
- `z_harm_s` (sensory-discriminative, Aδ-analog): proximity/intensity/location, forward-predictable
- `z_harm_a` (affective-motivational, C-fiber-analog): accumulated homeostatic deviation, motivational urgency

### ARC-033: Harm forward model for SD-003
A dedicated E2_harm_s(z_harm_s, action) → z_harm_s_next module, enabling SD-003 counterfactual attribution to operate within the harm stream without any cross-stream bridge.

---

## Implementation Scope (V3)

1. `CausalGridWorldV2`: emit `harm_obs_a` alongside existing `harm_obs` (renamed `harm_obs_s`)
   - `harm_obs_a` = EMA of `harm_obs_s` with τ = 10-30 steps (slow accumulation)
2. New `AffectiveHarmEncoder` in `ree_core/encoders/` or `ree_core/latent/`
3. `LatentState`/`LatentStackConfig`: add `z_harm_a` field alongside `z_harm`
4. New `E2_harm_s` forward model in `ree_core/predictors/` — same architecture as E2 world_forward but trained on harm stream
5. `E3Selector`: accept `z_harm_s` (discriminative, for attribution) and `z_harm_a` (affective, for commit gating) as separate inputs
6. `REEAgent`: wire dual harm streams throughout

Gating condition: SD-011 implementation depends on SD-010 being stable (it is: EXQ-056c, EXQ-058b PASS). ARC-033 (E2_harm_s) is a direct prerequisite for the next SD-003 experiment.

---

## Key Papers to Register

- Melzack, R. & Casey, K. L. (1968). Sensory, motivational, and central control determinants of pain. In Kenshalo (Ed.), *The Skin Senses*.
- Craig, A. D. (2002). Interoception: the sense of the physiological condition of the body. *Current Opinion in Neurobiology*, 13(4), 500-505.
- Craig, A. D. (2003). A new view of pain as a homeostatic emotion. *Trends in Neurosciences*, 26(6), 303-307.
- Craig, A. D. (2009). How do you feel? Interoception: the sense of the physiological condition of the body. *Nature Reviews Neuroscience*, 10(1), 59-70.
- Rainville, P., Duncan, G. H., Price, D. D., Carrier, B., & Bushnell, M. C. (1997). Pain affect encoded in human anterior cingulate but not somatosensory cortex. *Science*, 277(5328), 968-971.
- Keltner, J. R., Furst, A., Fan, C., Redfern, R., Inglis, B., & Fields, H. L. (2006). Isolating the modulatory effect of expectation on pain transmission. *J Neurosci*, 26(16), 4437-4443.
- Barrett, L. F. & Simmons, W. K. (2015). Interoceptive predictions in the brain. *Nature Reviews Neuroscience*, 16(7), 419-429.
