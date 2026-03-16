# Literature Summary: 2026-03-16_mech089_lisman_jensen_theta_gamma_neuron2013

## Claims Tested

- `MECH-089`

## Source

- Lisman JE, Jensen O (2013). *The Theta-Gamma Neural Code*. Neuron.
- DOI: `10.1016/j.neuron.2013.03.007`
- URL: `https://pmc.ncbi.nlm.nih.gov/articles/PMC3648857/`

## Source Wording

Gamma-frequency oscillations (~30-100 Hz) nest within theta cycles (~4-12 Hz) in the hippocampus; each theta cycle (~125 ms) contains ~5-7 gamma subcycles, each carrying a distinct spatial or sequential representation. The strength of theta-gamma coupling correlates directly with working memory performance and learning in spatial tasks. This phase-amplitude modulation is the basis of an ordered multi-item neural code where theta provides the temporal frame and gamma provides the item-specific carriers.

## REE Translation

MECH-089 (ThetaBuffer / cross-frequency coupling for inter-loop integration): The theta-gamma nesting architecture is the biological substrate for the REE ThetaBuffer. E1 updates at the sensory frame (gamma-equivalent) rate; E3 samples theta-cycle summaries rather than raw E1 output. This temporal packaging is what makes E3 harm estimates tractable — it operates on integrated context, not moment-to-moment sensory noise. The hippocampal-prefrontal extension of theta-gamma coupling in this review directly supports the claim that the packaging boundary defines the minimum temporal resolution for moral attribution in E3.

## Caveat

Evidence is primarily from rodent hippocampal spatial coding and hippocampal-mPFC circuits. Whether the same mechanism scales to prefrontal deliberative planning loops operating at a slower rate than theta (~8 Hz) requires caution. The theta rate may be faster than some conceptions of E3's deliberation rate; this rate mismatch should be addressed in V3 design.

## Direction and Confidence

- `evidence_direction`: `supports`
- `confidence`: `0.82`
