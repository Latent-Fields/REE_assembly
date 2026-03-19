# Sensory Stream Tags (Minimal Set)

**Claim Type:** architectural_commitment  
**Scope:** Minimal tagged sensory streams required for REE prediction, comparison, and action  
**Depends On:** INV-008 (precision is routed), INV-012 (commitment gates responsibility), ARC-004 (L-space), ARC-005 (control plane), ARC-003 (E3), ARC-015 (responsibility flow)  
**Status:** provisional  
**Claim ID:** ARC-017
<a id="arc-017"></a>

---

REE requires a minimal, explicit tagging of sensory streams so that prediction, prediction-comparison, and motor output
are the only privileged operations. Everything else is convolution, recombination, or temporal binding over these tagged
streams.

## Primary sensory stream tags (irreducible)

These streams must exist prior to learning and prior to semantics.

- `WORLD`: exteroceptive input (non-self sensory input; modality fusion may occur upstream). Multiple
  exteroceptive modalities (vision, audition, somatosensory/touch) each contribute differently to this
  stream's shared latent — see MECH-103.
- `HOMEOSTASIS`: interoceptive viability state (energy, temperature, hunger/thirst proxies, fatigue, suffocation).
- `HARM`: nociceptive or fast threat proxies (imminent violation of viability constraints). Operates via a
  dedicated parallel pathway — direct thalamic input to the harm-detection system (amygdala-equivalent)
  that bypasses E1 cortical processing entirely (the "low road"). This stream is not derived from z_world;
  it has its own sensory input and training signal. Reafference correction (SD-007) applies at this stream,
  not at z_world. See ARC-027.
- `SELF_SENSORY`: reafferent consequences of the system's own outputs (requires efference copy or equivalent).
  Includes both proprioceptive (joint/muscle state) and vestibular (spatial orientation, self-motion-in-space)
  components — see `VESTIBULAR` below.
- `VESTIBULAR`: spatial orientation, balance, and self-motion-in-space (semicircular canals, otolith organs).
  Distinct from proprioception (joint/muscle state) and WORLD (exteroceptive content). Grounds the egocentric
  spatial frame used by SELF_SENSORY and provides allocentric self-motion reference for z_self. Feeds
  SELF_SENSORY alongside proprioception; grounded in otolith → thalamus → PPC pathway.

Each stream is predicted and compared against observations. The tag determines how error is interpreted and routed.

## Secondary / derived stream tags (still required)

These are not raw senses but must be explicit tagged streams to preserve ethical coherence.

- `PRECISION`: trust/confidence over prediction errors; controls learning, attention, and commitment.
- `TEMPORAL_COHERENCE`: alignment across timescales; detects fragmentation and narrative collapse.
- `REALITY_COHERENCE`: provenance/authority/identity consistency signal generated from hippocampal trace structure and
  trusted control-store checks.
- `VALENCE`: ranking of predicted trajectories based on viability and coherence (not scalar reward).

These tags allow REE to remain robust without collapsing ethics into a reward channel.

## Channel typing overlay (authority-safe exteroception)

To keep stream separation enforceable under prompt-injection pressure, REE should carry typed exteroceptive payloads:

- `OBS`: observations from user text, tools, or sensors.
- `INS`: task requests/instructions with externally supplied intent.
- `POL`: invariant/policy payloads (trusted internal only).
- `ID`: system identity and role anchors (trusted internal only).
- `CAPS`: capability/permission manifests (trusted internal only).

Routing constraints:

- External channels can emit `OBS` and `INS`, never `POL`, `ID`, or `CAPS`.
- Tool output is `OBS` by default unless explicitly elevated by a trusted internal capability gate.
- `WORLD` updates representation and hypothesis generation, but cannot directly write policy, identity, or capability
  stores.
- Commitment remains gated: no direct `WORLD` -> privileged commit path without verification and veto checks.

<a id="mech-035"></a>
## VALENCE as Vector Ranking (MECH-035)

**Claim Type:** mechanism_hypothesis  
**Scope:** Vector-valued valence used for non-scalar trajectory ranking  
**Depends On:** ARC-017, ARC-003, ARC-005  
**Status:** candidate  
**Claim ID:** MECH-035

VALENCE is defined as a vector of predicted deltas across tagged streams (e.g., HOMEOSTASIS, HARM,
TEMPORAL_COHERENCE, SELF_IMPACT error, option volume, inferred other welfare). Trajectory selection ranks candidates
using constraint-first and Pareto/lexicographic comparison rather than collapsing the vector to a scalar. This
preserves non-scalar ethics and avoids reward-style collapse.

## Motor and self-impact streams

- `ACTION`: all interventions the system can make.
- `SELF_IMPACT`: comparison between predicted and observed self-generated consequences.

`SELF_IMPACT` is the minimal substrate of internal responsibility: it is where reafference becomes self-attribution.

## Social extension tags (derived, multi-agent)

REE does not require social tags for single-agent viability, but multi-agent settings can add derived tags over WORLD:

- `AGENCY`: detects interveners vs passive dynamics.
- `OTHER_SELFLIKE`: probability that an agent runs a self/world separation + self-impact loop.
- `OTHER_HARM`: estimated harm-to-other (computed when `OTHER_SELFLIKE` is high).
- Optional `AFFILIATION`: stabilises coupling based on history/kinship.

These reuse self/world/impact machinery and are routed by control-plane coupling (see `social.md`).
They are not primitive senses and do not add a new cognitive subsystem.

## Mapping streams onto engines (E1/E2/E3 + hippocampus)

- **E1** maintains slow structure and long-horizon HOMEOSTASIS/TEMPORAL_COHERENCE priors. Receives WORLD stream
  as primary input; multimodal exteroceptive fusion occurs here (MECH-103).
- **E2** provides fast prediction and reafference comparison for SELF_SENSORY/SELF_IMPACT. Receives proprioceptive
  and vestibular components of SELF_SENSORY alongside efference copy.
- **Harm-detection system (amygdala-equivalent)** receives HARM stream directly via parallel thalamic pathway,
  independent of E1. Outputs a harm signal that feeds into E3 as an input, not a derived head inside E3 (ARC-027).
- **Vestibular system** grounds egocentric spatial frame; feeds SELF_SENSORY alongside proprioception via
  otolith → thalamus → PPC pathway. Supports z_self spatial orientation component.
- **Hippocampal systems** construct explicit counterfactual trajectories and provenance bindings; E1/E2 supply
  constraints and seeds.
- **Reality-coherence loop (RC)** computes `REALITY_COHERENCE` conflict from hippocampal provenance, trusted identity,
  and policy consistency checks.
- **E3** applies vetoes and ranks trajectories via VALENCE, then commits; commitment tags intended action for
  self-impact learning while consuming RC conflict and harm-detection output as gate inputs.

## Explicit exclusions

REE does not require primitive emotion categories, symbolic goals, language, social cognition, moral rules,
utility functions, or explicit self-narratives. These can emerge from convolutions over the streams above.

## Why this set is sufficient

If REE supports prediction and prediction-comparison on all tagged streams, precision-weighted updating,
and ACTION -> SELF_SENSORY -> SELF_IMPACT loops, then it acquires:

- A distinction between self and world
- A notion of harm vs drift vs opportunity
- Temporal continuity signals
- Reality/provenance consistency signals for authority-sensitive commitment
- An internal responsibility signal
- Reward-like dynamics as emergent, vector-valued signals rather than a reward channel

Reward-like effects arise from improved HOMEOSTASIS/HARM predictions, increased TEMPORAL_COHERENCE,
expanded viable trajectory volume, and low self-impact error, without introducing an explicit reward scalar.
These signals remain **read-only**; they must not become a control channel.

---

## Open Questions

None noted in preserved sources.

## Related Claims (IDs)

- ARC-017
- ARC-025
- ARC-003
- ARC-004
- ARC-005
- ARC-015
- INV-008
- INV-012
- MECH-035
- MECH-037
- MECH-064
- MECH-065
- MECH-103

## Three-Stream Biological Mapping (added 2026-03-17)

HCP connectome analysis (Haak & Beckmann 2018, Cortex 98:73–83, n=470) confirmed three
anatomically distinct visual pathways — not the classical two. These map directly onto
ARC-017 stream tags:

| Biological stream | White matter | REE stream tag | Engine |
|---|---|---|---|
| Dorsal (IPS/occipitoparietal) | SLF I/II | `SELF_SENSORY` | E2 (z_self) |
| Ventral (VO/PHC) | Ventral occipitotemporal | `WORLD` | E1/E3 (z_world content) |
| Lateral/third (MT→MST→STS) | Lateral STS pathway | `AGENCY` / `HARM` | E3 harm channel |
| Vestibular (otolith→VN→thalamus) | Thalamo-parietal (VPLc→PPC) | `VESTIBULAR` | E2 (z_self spatial frame) |
| Nociceptive (spinothalamic, low road) | Thalamo-amygdala (VPM/Po→amygdala) | `HARM` (parallel) | Harm-detection (ARC-025) |

Key implication: the `SELF_SENSORY` tag (reafferent consequences of own motor output)
corresponds to the dorsal stream + efference copy pathway (premotor → PPC via SLF,
confirmed by Rolls et al. 2023 HCP 7T tractography). The lateral/third stream — specialised
for dynamic motion and biological motion — terminates near TPJ and feeds the agency/harm
detection channel (MECH-095, MECH-099) rather than the world-content representation.

This anatomically grounds MECH-069 (incommensurability): the three error signals are
incommensurable in part because they run on physically distinct hardware with distinct
white matter tracts. See `docs/thoughts/2026-03-17_three_stream_reafference.md` and
`evidence/literature/targeted_review_reafference_streams/`.

<a id="mech-103"></a>
## Multimodal Exteroception Fusion into E1 World Latent (MECH-103)

**Claim Type:** mechanism_hypothesis
**Scope:** How multiple exteroceptive modalities contribute to E1's shared world latent
**Depends On:** ARC-017, ARC-004
**Status:** candidate
**Claim ID:** MECH-103

Different exteroceptive modalities (vision, audition, somatosensory/touch) each contribute differently to E1's
shared world latent (`z_S` / `z_world`). Multi-source convergence — rather than single-modality input — produces
more accurate and robust world representations because each modality carries complementary structure:

- **Vision**: object identity, spatial layout, scene structure
- **Audition**: events, temporal cues, off-screen dynamics
- **Somatosensory/touch**: surface properties, contact, texture

Modalities do not merge identically — each has its own encoder pathway into the shared latent, contributing
weighted evidence depending on reliability and context (precision-gated). This grounds the `WORLD` stream
tag's parenthetical "modality fusion may occur upstream" in a concrete mechanism.

Biological grounding: superior temporal sulcus (STS) is a primary multisensory convergence zone; MST integrates
optic flow with vestibular and auditory input. Analogous cross-modal binding occurs across the ventral stream
for object identity (Murray et al. 2004).

---

<a id="arc-027"></a>
## Nociception as Parallel Sensory Pathway (ARC-027)

**Claim Type:** architectural_commitment
**Scope:** HARM stream must be implemented as an independent parallel sensory pipeline
**Depends On:** ARC-017, ARC-003
**Status:** candidate
**Implementation Phase:** v3
**Claim ID:** ARC-027
**Note:** Previously misregistered as ARC-025 (ID collision with three_engine_irreducibility). Corrected 2026-03-19.

The HARM stream must be implemented as a parallel sensory pathway with its own sensory input and training
signal, not derived from z_world or E1 processing. It receives direct thalamic input (fast, coarse threat
detection — the "low road") that feeds the amygdala-equivalent harm-detection system before cortical
world-model processing occurs.

This architectural constraint has several downstream implications:

- **harm_eval is an input to E3**, not a head inside E3. E3 receives harm signal from the harm-detection
  system as a constraint on trajectory ranking and commitment gating.
- **SD-007 reafference correction** applies at the HARM stream level (was this nociceptive signal caused by
  the agent's own action?), not at z_world. The over-correction observed in EXQ-027b is explained: we were
  applying reafference to the wrong signal.
- **SD-003 attribution** (self-caused vs world-caused harm) compares the HARM stream signal against E2's
  counterfactual rollout. The two streams converge for attribution; attribution is not internal to E3.
- **The EXQ-043/044 calibration collapses** are explained: those experiments trained a sensory detection
  system through a planning pipeline (harm_eval head on z_world), which is architecturally incorrect. A
  dedicated HARM stream with its own training signal would not exhibit this failure mode.

Biological grounding: the spinothalamic tract provides fast nociceptive input direct to the amygdala
(thalamo-amygdala projection via VPM/Po nuclei) in parallel with the slower cortical route
(thalamus → S1 → insula → amygdala). The amygdala's rapid threat response depends on the direct pathway
(LeDoux 1996, "low road"). This is anatomically and functionally distinct from the cortical world-model
processing pathway.

---

## References / Source Fragments

- `docs/thoughts/2026-02-08_sensory_stream_tags.md`
- `docs/thoughts/2026-02-09_valence_vector.md`
- `docs/thoughts/17-02-26_necessary_separations_based_on_considering-prompt_injection.md`
- `docs/thoughts/2026-02-17_control_plane_update.md`
- `docs/thoughts/2026-03-17_three_stream_reafference.md`
