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

- `WORLD`: exteroceptive input (non-self sensory input; modality fusion may occur upstream).
- `HOMEOSTASIS`: interoceptive viability state (energy, temperature, hunger/thirst proxies, fatigue, suffocation).
- `HARM`: nociceptive or fast threat proxies (imminent violation of viability constraints).
- `SELF_SENSORY`: reafferent consequences of the system's own outputs (requires efference copy or equivalent).

Each stream is predicted and compared against observations. The tag determines how error is interpreted and routed.

## Secondary / derived stream tags (still required)

These are not raw senses but must be explicit tagged streams to preserve ethical coherence.

- `PRECISION`: trust/confidence over prediction errors; controls learning, attention, and commitment.
- `TEMPORAL_COHERENCE`: alignment across timescales; detects fragmentation and narrative collapse.
- `VALENCE`: ranking of predicted trajectories based on viability and coherence (not scalar reward).

These tags allow REE to remain robust without collapsing ethics into a reward channel.

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

- **E1** maintains slow structure and long-horizon HOMEOSTASIS/HARM/TEMPORAL_COHERENCE priors.
- **E2** provides fast prediction and reafference comparison for SELF_SENSORY/SELF_IMPACT.
- **Hippocampal systems** construct explicit counterfactual trajectories; E1/E2 supply constraints and seeds.
- **E3** applies vetoes and ranks trajectories via VALENCE, then commits; commitment tags intended action for
  self-impact learning.

## Explicit exclusions

REE does not require primitive emotion categories, symbolic goals, language, social cognition, moral rules,
utility functions, or explicit self-narratives. These can emerge from convolutions over the streams above.

## Why this set is sufficient

If REE supports prediction and prediction-comparison on all tagged streams, precision-weighted updating,
and ACTION -> SELF_SENSORY -> SELF_IMPACT loops, then it acquires:

- A distinction between self and world
- A notion of harm vs drift vs opportunity
- Temporal continuity signals
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
- ARC-003
- ARC-004
- ARC-005
- ARC-015
- INV-008
- INV-012
- MECH-035

## References / Source Fragments

- `docs/thoughts/2026-02-08_sensory_stream_tags.md`
- `docs/thoughts/2026-02-09_valence_vector.md`
