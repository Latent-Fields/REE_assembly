# The hippocampal–VTA loop (Lisman & Grace 2005) — MECH-149 + MECH-075

**Claims:** MECH-149 — CA1 mismatch between E1-predicted and CA3-retrieved z_world gates hippocampal trajectory injection into E3 (novel → more, more-diverse proposals; familiar → cached viability). MECH-075 — basal-ganglia/dopaminergic gain sets the threshold on hippocampal attractor dynamics.

## What the paper did

Lisman and Grace synthesised anatomy and physiology into a now-canonical model: the hippocampus and the dopaminergic neurons of the ventral tegmental area form a closed functional **loop**. The loop is activated when the hippocampus detects information that is *not already stored* — a novelty signal. That signal is routed through the subiculum, nucleus accumbens, and ventral pallidum to the VTA, where it combines with salience and goal information to drive novelty-dependent dopamine firing. In the return arm, dopamine is released back into the hippocampus, enhancing long-term potentiation and learning. Novelty, in this scheme, regulates what is allowed to enter long-term memory.

## Why it matters for REE

This single review grounds two REE claims at once, and — importantly for the assembly sweep — shows that they are **not independent claims but two arms of one circuit**. MECH-149 needs a hippocampal mismatch/novelty detector: the "is this already predicted/stored?" computation that the paper places at the front of the loop. MECH-075 needs a dopaminergic gain control over hippocampal dynamics: the return arm of the same loop, where VTA dopamine modulates hippocampal excitability and plasticity. So the completion-set partner that the HPL-9 node flagged for MECH-149 (the VTA loop, MECH-075) is grounded here in the same source — building a CA1 mismatch gate without the dopaminergic gain arm would sever the feedback that, biologically, makes the novelty signal *do* anything.

## Caveats and confidence

Two honest limits. First, this is a theoretical/review synthesis, not a single primary result — its authority comes from being a heavily-cited, influential framework rather than from one decisive experiment. Second, and more substantively, the loop as described gates **entry into long-term memory** — what gets *stored*. MECH-149 repurposes the very same novelty signal to gate **rollout injection** — what gets *simulated* in the planner. The novelty-detection arm transfers cleanly (a mismatch computation is a mismatch computation), but the downstream consumer is REE-specific, and the claim's specific prediction (high mismatch → more *and more diverse* proposals; low mismatch → fall back on *cached* viability) is an extension the paper does not test. With those caveats the support is real and the dual grounding is valuable. Confidence 0.74 (supports), with the planning-injection consumer noted as the boundary.

*According to PubMed.* Source: Lisman JE, Grace AA (2005), *Neuron* 46(5):703–13. [DOI](https://doi.org/10.1016/j.neuron.2005.05.002)
