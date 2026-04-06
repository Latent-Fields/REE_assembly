# Evidence for area CA1 as a match/mismatch detector

**Duncan, Ketz, Inati & Davachi, 2011, Hippocampus**

## What the paper does

Duncan et al. used high-resolution fMRI to examine hippocampal subfield responses while participants retrieved learned scene-object pairs from memory and were tested with probes containing 0 to 4 feature changes. The key manipulation was varying both the number of changes and their task relevance, allowing the authors to distinguish automatic mismatch detection from deliberate change evaluation.

## Key findings relevant to MECH-205

CA1 was the only hippocampal subfield to reliably track the total number of stimulus changes, doing so roughly linearly and automatically regardless of whether changes were task-relevant or task-irrelevant. This automatic, graded sensitivity to deviation from expectation is the hallmark of a comparator, not a detector of specific features. The interpretation is that CA1 receives CA3's pattern-completed prediction on one input channel and current sensory reality via entorhinal cortex on another, and its activity reflects the degree of discrepancy between them.

This is a foundational result for MECH-205's contrastive causal structure. The contrastive replay posited in MECH-205 requires a biological mechanism that can hold two things simultaneously — the anchor episode (what was expected) and the variation (what actually happened or what is being simulated) — and compute their difference as a learning signal. Duncan et al. provide evidence that CA1 is precisely this mechanism, operating automatically and in proportion to the magnitude of the discrepancy.

## Mapping to MECH-205

During offline contrastive replay, the hippocampus generates variations around the anchor episode via E2 rollouts. For each variation, the system needs to compute: "how does this variation differ from the anchor?" and "does this variation produce the surprising outcome or not?" The CA1 comparator function, applied to replayed (rather than perceived) episodes, would implement exactly this. CA3 pattern-completes the anchor; E2-generated variations are fed via entorhinal input; CA1 computes the difference. The contrastive learning signal is the output of CA1's comparator across the variation population.

The graded, linear sensitivity to number of changes matters: it means the comparator provides a *quantitative* mismatch signal, not a binary match/mismatch flag. This is what MECH-205 needs — a continuous priority signal that can rank variations by how different they are from the anchor, enabling structured causal feature extraction.

## Limitations

This is a 2011 paper with fMRI resolution that is good for its time but lower than current ultra-high-field standards. The comparator function is demonstrated for online waking perception; whether it operates in the same way during offline SWR-driven replay is an inference. The transfer from online perception to offline replay is the key gap: during SWRs, CA1 receives compressed sequential input from CA3, not direct sensory input from entorhinal cortex in the same way as waking perception.

## Confidence reasoning

Foundational result in a good journal; the CA1-as-comparator interpretation is well-cited and replicated. Mapping fidelity moderate — the mechanism is right but the context (online vs offline) differs. Overall confidence 0.68.
