# Summary: Morton, Schlichting & Preston (2020)

**Citation:** Morton NW, Schlichting ML, Preston AR. "Representations of common event structure in medial temporal lobe and frontoparietal cortex support efficient inference." *Proc Natl Acad Sci USA* 117(47):29338-29345. DOI: [10.1073/pnas.1912338117](https://doi.org/10.1073/pnas.1912338117)

## What the paper did

fMRI study of how the brain extracts and uses abstract representations of common event structure (schema) to support novel decisions. Participants learned overlapping paired associates (AB, BC) from triads (ABC) sharing the same internal structure, then were tested on indirect (AC) inferences.

## Key findings

1. **Common geometric structure forms spontaneously** -- hippocampal and frontoparietal regions encoded cross-triad relationships with a consistent geometric structure even without explicit reinforcement.
2. **Parahippocampal cortex is hierarchical** -- it represents both cross-triad relational structure (schema) and distinctions between individual triads (slot-level). This is the structural prerequisite for efficient slot-filling.
3. **Pattern completion vs. vector-based retrieval are dissociable** -- hippocampus supports pattern completion; parahippocampal cortex and lateral parietal cortex support vector-based retrieval for inference.
4. **Common structure accelerates inference** -- shared relational geometry enables faster AC inference, confirming that schema (common structure) enables efficient slot-filling (inference from slots).

## Relevance to INV-044

The paper provides neural and computational evidence for the two-stage architecture that INV-044 claims is architecturally necessary:
- **Stage 1 (schema/prior):** Cross-triad common geometric structure must exist before efficient inference. This is the prior -- which structural relationships are relevant.
- **Stage 2 (slot-filling/posterior):** Vector-based retrieval using the geometric prior to fill triad-specific slots. This is posterior inference -- which specific evidence belongs to which slot.

The parahippocampal hierarchy that encodes both levels is the neural substrate for INV-044's claim: schema structure (cross-triad geometry) must be installed before attribution (slot-specific retrieval) can be informative.

## Limitations for REE mapping

- Does not directly test the failure mode: no condition where schema and slot-filling are co-computed
- The temporal ordering (prior installation before slot-filling) is inferred from representational geometry, not manipulated
- Domain is associative spatial inference; transfer to REE causal attribution is structural/analogical
