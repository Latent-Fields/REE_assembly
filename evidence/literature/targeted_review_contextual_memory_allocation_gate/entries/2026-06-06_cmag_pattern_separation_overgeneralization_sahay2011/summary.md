# Sahay et al. 2011 -- Increasing adult hippocampal neurogenesis is sufficient to improve pattern separation

**Claim under review:** CANDIDATE-contextual-memory-allocation-gate (V4/V5 intake, 2026-06-06)
**Direction:** supports (biological motivation for a false-linking-risk cost) | **Confidence:** 0.70

## What the paper did

Sahay, Hen and colleagues built a genetic strategy to selectively increase the survival of adult-born dentate granule cells, isolating neurogenesis from the many other variables that usually co-vary with it. Mice with more functionally integrated adult-born neurons were *better at discriminating between two similar contexts* in contextual fear conditioning and in a touchscreen spatial-discrimination task -- the behavioural signature of improved pattern separation. The companion framing in this literature (and the authors' own discussion) is that the converse, impaired separation, produces *overgeneralization*: distinct experiences that should be kept apart are instead treated as the same, a pattern repeatedly invoked as a transdiagnostic endophenotype of mood, anxiety, trauma-related and age-related disorders.

## Why it matters for the intake

This is the anchor that addresses the intake's third verdict question: is a reality-coherence / false-linking-risk *cost* biologically motivated? Sahay 2011 supplies the affirmative case. When separation is too weak, the system over-links -- and that over-linking is shown to be costly and behaviourally maladaptive, not a neutral outcome. This grounds the `estimate_false_linking_risk(...)` penalty in the intake's `allocate_memory_trace` sketch: a principled allocation gate should price the risk that integrating a new trace corrupts the distinctness of an existing one. It also lends cautious, mechanism-level support to the intake's psychiatric speculation (Section 6, Q5) that weak separation combined with high salience underlies false association -- though that remains speculation, and the project's psychosis/confabulation-distinction memory warns against collapsing these failure modes.

## Limitations and caveats

The cost here is demonstrated as the failure of a separation *effector* (DG neurogenesis), not as an explicit control-plane cost term. So the paper motivates *that* false linking is costly; it does not show a controller *pricing* that risk at allocation time -- which is precisely the novel REE lever. The readout, contextual fear discrimination, is an indirect proxy for "inappropriate linking of unrelated memories." And critically, the paper measures only the *under-separation* pole. The intake brackets the gate between two failure modes -- over-integration (false association) and over-separation (failure to generalize) -- but Sahay evidences only the first. A REE cost term modelled on this paper alone would be one-sided and would bias the gate toward separation; the over-separation cost has to be sourced from the generalization/schema literature (e.g. Tse 2007 in this same review, which shows the *benefit* of integration).

## Confidence reasoning

Source quality is high (Nature, causal genetic manipulation, foundational for the neurogenesis-separation-overgeneralization link). Mapping fidelity is moderate: it motivates a false-linking cost but through an effector-failure readout rather than a control cost term, and only for one of the two poles. Transfer risk is moderate-to-high (rodent fear discrimination to a general reality-coherence cost in an artificial agent; the transdiagnostic clinical framing raises it further). Net 0.70 -- enough to say the cost is biologically motivated, not enough to specify its form.
