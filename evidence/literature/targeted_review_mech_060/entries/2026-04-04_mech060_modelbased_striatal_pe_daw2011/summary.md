# Literature Summary: 2026-04-04_mech060_modelbased_striatal_pe_daw2011

## Claims Tested

- `MECH-060`

## Source

- Daw ND, Gershman SJ, Seymour B, Dayan P, Dolan RJ (2011), *Model-based influences on humans' choices and striatal prediction errors*. Neuron 69(6): 1204-1215.
- DOI: 10.1016/j.neuron.2011.02.027
- PMID: 21435563
- URL: https://pubmed.ncbi.nlm.nih.gov/21435563/

## Mapping to REE

MECH-060 requires that the pre-commit simulation channel and the post-commit realized-error channel stay responsibility-distinct. Implicit in this requirement is the assumption that such a distinction is architecturally feasible -- that a system can, in principle, keep the two error streams segregated. The Glascher et al. (2010) study provides one line of evidence for this. Daw et al. (2011) provides an important complication.

Using a two-step Markov decision task carefully designed to dissociate model-based from model-free choice influences, Daw and colleagues find that the ventral striatal BOLD signal does not carry a pure model-free prediction error as previously assumed. Instead, ventral striatum reflects a mixture of model-free and model-based (i.e., prospective/simulational) prediction error in proportions that match the mixture governing behavioral choice. The implication is that the brain does not simply segregate its two learning systems into anatomically pure substrates -- the prospective computation from the model-based system bleeds into the ventral striatal signal that is often treated as the realized-outcome channel.

From a MECH-060 perspective, this is a mixed result. On one reading, it challenges the biological necessity of strict channel separation: if the brain mixes channels at the level of ventral striatum without apparent dysfunction, then strict write-boundary enforcement may be an engineering choice that exceeds what biology requires. On another reading, the mixing could itself represent a failure mode that explains known irrationalities in human decision-making -- and the REE architecture, by enforcing the boundary, may achieve a cleaner separation than the biological system manages. The paper does not adjudicate between these interpretations.

The study is important background for MECH-060 because it establishes that channel blending is detectable, measurable, and relates to behavioral signatures (the proportion of model-based vs. model-free influence on behavior tracks the proportion of mixing in the neural signal). This is circumstantial support for the MECH-060 argument that write-boundary contamination should be detectable -- which the REE EXQ-005 experiment confirmed directly.

## Caveats and Mapping Limits

- The paper studies learning and choice in a two-step sequential decision task, not harm attribution or residue field update. The MECH-060 domain (ethical harm tracking) is considerably more specific.
- Channel mixing in ventral striatum is interpreted as a feature of adaptive arbitration, not as a bug. This weakens the case that mixing is necessarily harmful.
- The study does not test the consequence of manipulating the mixing -- it observes natural variation, which limits causal inference about what channel separation achieves.

## Direction and Confidence

- `evidence_direction`: `mixed`
- `confidence`: `0.55`
- Rationale: the study documents biological channel mixing of prospective model-based and retrospective model-free signals in ventral striatum -- relevant background for MECH-060 but does not directly test write-boundary enforcement or show that strict separation is necessary; rated mixed because the finding is consistent with both adaptive mixing and with contamination being a tractable problem.
