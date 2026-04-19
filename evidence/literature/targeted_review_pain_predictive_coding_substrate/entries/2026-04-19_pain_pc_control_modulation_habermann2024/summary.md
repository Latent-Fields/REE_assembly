# Habermann, Strube & Buchel 2024 -- How control modulates pain

**Citation.** Habermann M, Strube A, Buchel C. How control modulates pain. Trends in Cognitive Sciences 2024; 29(1): 60-72. [DOI](https://doi.org/10.1016/j.tics.2024.09.014). (According to PubMed.)

**What they did.** A 2024 review from the Buchel lab synthesising how perceived control over pain changes pain perception. They sketch a taxonomy of control types, integrate control into a Bayesian pain model, and describe the neural substrate.

**Key finding.** Control reduces pain through changes in expectation and in the precision assigned to expectations. The anterior insula, middle frontal gyrus, and ACC are the substrate. The computational primitive is precision-weighted integration -- the same machinery that Geuter 2017 and Fazeli 2018 identified for expectation-modulated pain, now extended to cover controllability effects.

**What this does for the REE question.** It validates the precision-weighted PE formulation in MECH-258 specifically: pain enters the dACC-analog as precision * PE, and precision is itself a function of controllability and context. This is directly what MECH-258's functional_restatement says.

Indirect but relevant: if the ACC/AIC axis is doing precision-weighted integration over a pain forward model, that model's internal architecture has to support precision modulation per-stream. Under a fully parallel two-model design, each would need its own precision machinery. Under a shared-trunk design, precision could be applied per-head or at the trunk level. The review does not force a decision, but the parsimony of maintaining a single precision-weighted substrate argues mildly for shared trunk.

**Limitations.** Review, not primary data. Does not address within-pain stream separation.

**Confidence reasoning.** Source quality is high (Trends in Cognitive Sciences, current review). Mapping fidelity moderate because the paper addresses the precision-weighting piece of MECH-258 rather than the shared-substrate decision for SD-032b directly.
