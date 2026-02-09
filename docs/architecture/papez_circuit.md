# Papez Circuit (Functional Analog)

**Claim Type:** mechanism_hypothesis  
**Scope:** Provenance gating / reality filtering via a Papez-like loop  
**Depends On:** ARC-007, ARC-018, ARC-003, ARC-005  
**Status:** candidate  
**Claim ID:** MECH-037
<a id="mech-037"></a>

---

REE can treat a **Papez-like loop** as a functional **reality-filtering / provenance-gating** mechanism rather than a
direct anatomical claim. The core idea is that E1-generated content should not reach high-precision commitment unless it
is supported by hippocampal trace structure and temporal ordering signals. This gate reduces confabulation-like failure
where internally generated content is treated as real without adequate provenance.

## Operational interpretation

- **Provenance gating:** E1 hypotheses are held at low precision unless a hippocampal trace / ordering signal is present.
- **Commitment filter:** E3 commitment is licensed only when provenance gating is satisfied.
- **Control-plane bias:** the control plane can down-weight untraced content or mark it as speculative.

## Failure mode

When provenance gating fails, E1 content can be committed without trace support, producing confabulation-like behavior:
high-confidence narratives that lack appropriate temporal or source grounding.

## Operational checklist

- **Input signals:** hippocampal trace presence, temporal ordering confidence, and recency flags.
- **Gate decision:** if trace/ordering support is low, down-weight precision and mark content as speculative.
- **Commitment rule:** E3 commitment requires provenance gate pass for E1-derived content.
- **Control-plane knobs:** tune sensitivity (false positive vs false negative tolerance) per mode.
- **Failure cues:** rising incoherence + high-confidence claims without trace support.

## Notes

This is a **functional analog** inspired by the Papez circuit’s role in memory networks and confabulation studies, not a
one-to-one anatomical mapping.

---

## Open Questions

None noted in preserved sources.

## Related Claims (IDs)

- MECH-037
- ARC-007
- ARC-018
- ARC-003
- ARC-005
- MECH-034

## References / Source Fragments

- `docs/thoughts/2026-02-09_papez_circuit_reality_filtering.md`
