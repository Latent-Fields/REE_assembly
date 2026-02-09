# Thoughts: VALENCE as a Vector Ranking Signal

Status: processed

Processed in:
- `docs/architecture/sensory_stream_tags.md` (MECH-035)

---

Related claims: ARC-017, ARC-003, ARC-005, MECH-035

VALENCE should be treated as a **vector of predicted deltas** over tagged streams (e.g., HOMEOSTASIS, HARM,
TEMPORAL_COHERENCE, SELF_IMPACT error, option volume, inferred other welfare). Trajectory selection should rank
candidates via constraint-first and Pareto/lexicographic comparison rather than collapsing to a scalar.

## Possible affected components

- Sensory stream tags / VALENCE definition (ARC-017)
- Trajectory selection ranking (ARC-003)
