# Thoughts: Minimal Sensory Stream Tags

Status: processed

Processed in:
- `docs/architecture/sensory_stream_tags.md` (ARC-017)

---

Related claims: ARC-003, ARC-004, ARC-005, ARC-015, INV-008, INV-012

Below is a minimal, sufficient set of sensory-stream tags for REE. Prediction, prediction-comparison, and motor output
are the only privileged operations; everything else is convolution, recombination, or temporal binding.

Primary tags: WORLD, HOMEOSTASIS, HARM, SELF_SENSORY.
Derived tags: PRECISION, TEMPORAL_COHERENCE, VALENCE.
Motor/self-impact: ACTION, SELF_IMPACT.

Explicit exclusions: no primitive emotions, goals, language, social cognition, moral rules, utility functions, or
self-narratives. These emerge from stream convolutions.

Reward-like dynamics are secondary phenomena from viability/coherence improvements, not an explicit reward channel.

## Possible affected components

- Control plane precision routing (ARC-005)
- Responsibility flow (ARC-015)
- E3 commitment and action (ARC-003)
- L-space stream separation (ARC-004)
- Precision routing invariant (INV-008)
- Commitment-responsibility invariant (INV-012)
