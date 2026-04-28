# Zhou, Montesinos-Cartagena, Wikenheiser, Gardner, Niv & Schoenbaum (2019) -- Complementary HPC and OFC Task Structure Representations

## What the paper did

This is the companion paper to Zhou 2019 (Current Biology, 29(6)) on rat OFC. The authors recorded single-unit ensembles from CA1 of the hippocampus during the same 24-position odour sequence task they had used to characterise OFC. They then directly compared the task-state codes carried by the two regions on a within-paradigm basis. The motivating question was whether HPC carries a comprehensive cognitive map while OFC carries a goal-relevant subset, as a popular formulation suggests.

## Key findings relevant to MECH-263

The expectation going in was that HPC would distinguish a richer set of task states than OFC, because hippocampus is the canonical cognitive-map structure and OFC is widely viewed as an outcome-prediction region. The result was more nuanced. HPC ensembles -- like OFC -- failed to distinguish states when distinguishing them was not behaviourally necessary. Both regions are selective. However, hippocampal ensembles were better than OFC at distinguishing states that required prospective memory for future task performance. The authors interpret this as a complementary division of labour: in familiar environments, OFC maintains the subject's current position on the cognitive map, while HPC supports that position when memory demands are high.

## How this maps to REE

MECH-263 specifies that SD-033b's cognitive map carries "what structural roles each state plays in the current task" -- a behaviour-relevant rather than exhaustive enumeration. Zhou 2019b's finding that OFC selectively distinguishes states that matter for behaviour is consistent with this framing. The HPC/OFC complementarity finding is also useful for ree-v3's overall architecture. SD-004 (held for V3) names the hippocampal module as the broader task-representation substrate. SD-033b (the OFC analogue) is the specific-outcome predictor that E2 queries. The Zhou complementarity finding gives an empirical grounding for this architectural division: HPC carries the broader prospective task representation, OFC reads from a more selective task-relevant subspace. The two are not redundant, and they should not be merged in the V3 design.

## Limitations and caveats

This paper supports the SELECTIVITY framing of MECH-263 but does not test its core architectural claim about the value/identity dissociation. It is supportive context for the SD-033b vs hippocampal-module division of labour rather than direct evidence for MECH-263's falsifiability criteria. The HPC/OFC division of labour interpretation is the authors' framing -- alternative readings are possible (e.g. HPC carries higher temporal-context resolution rather than prospective memory specifically). The species and modality transfer is the standard rat-single-unit chain.

## Confidence reasoning

I have set this at 0.78. Source quality is high (Current Biology, Niv-Schoenbaum lab, clean within-paradigm cross-region comparison). Mapping fidelity is moderate -- the paper supports MECH-263's framing of SD-033b's selectivity but does not directly test the value/identity dissociation that is the claim's load-bearing architectural commitment. Transfer risk is the standard rat-to-REE chain. The reason it is not higher is that the paper is more about scaffolding than core evidence; the reason it is not lower is that the within-paradigm cross-region comparison is methodologically among the cleanest available and directly supports REE's architectural separation of SD-033b from the hippocampal module.

## Citation

According to PubMed, DOI: [10.1016/j.cub.2019.08.040](https://doi.org/10.1016/j.cub.2019.08.040). PMID 31588004.
