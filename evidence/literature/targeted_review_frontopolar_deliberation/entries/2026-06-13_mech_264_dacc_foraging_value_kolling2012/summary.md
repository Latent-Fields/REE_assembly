# Kolling et al 2012 -- ACC foraging/search value as the dACC<->FPC loop partner

**Claims:** MECH-264, SD-046, SD-032b (cross-link)
**Direction:** supports (loop-level grounding)
**Confidence:** 0.71

## What the paper did

Kolling, Behrens, Mars & Rushworth used human fMRI to dissociate two modes of choice. In **comparative** decision-making, ventromedial prefrontal cortex (vmPFC) encodes the values of specific, well-defined options. In **foraging** -- the sequential "stay with this or search elsewhere?" problem -- anterior cingulate cortex (ACC) encodes a different quantity: the average value of the foraging *environment* and the *cost* of searching for alternatives, in an invariant reference frame anchored to "search for alternatives." The key result is that switch/search value and chosen-option value are computed by anatomically and representationally distinct systems.

## Findings relevant to the claims

The goal-deliberation roadmap (GDL-8) explicitly asks for this paper as the **dACC<->FPC loop** partner, and that is exactly what it grounds:

- **MECH-264 (switch-to-alternative gate).** MECH-264 specifies that when the counterfactual-option value exceeds the chosen-option value by a threshold-sensitive margin, the system signals a switch. Kolling's ACC foraging-value signal *is* the neural quantity that drives this switch -- the value of leaving the current course for the environment's alternatives. The per-option counterfactual value MECH-264 maintains is the Boorman 2009 lateral-FPC signal (already grounded in prong_d); this paper supplies the complementary **environment/search-value** term and shows the two live in different substrates.
- **SD-032b (dACC-analog adaptive control).** This is the V3 hook the roadmap names. Kolling localises foraging/search value to ACC, which is SD-032b's subject. So the entry doubles as grounding for the dACC-analog's role in slot-switching arbitration.
- **SD-046 (multi-slot arbitration).** SD-046's "dACC-style arbitrator selects which slot's best trajectory commits this tick" is the multi-goal generalisation of exactly this stay-vs-search computation.

Together these make the co-constitutive point the node was after: counterfactual deliberation is not one module. It is a **loop** -- FPC holds the specific alternative's value (Boorman/MECH-264), ACC holds the environment/search value (Kolling/SD-032b), and the comparison between them gates the switch.

## Limitations and caveats

The mapping is honest only at the *loop* level. The paper's switch-value signal is in ACC, not FPC, so it grounds SD-032b and the loop rather than SD-033e/MECH-264's frontopolar locus directly -- I tag MECH-264 because the switch-gate it specifies is what ACC value drives, not because the paper measured an FPC counterfactual. There is also a live controversy: Hayden and colleagues argued some "ACC foraging value" effects can be re-described as choice difficulty / response conflict. If a V4 switch gate fired on conflict alone it would reproduce that confound rather than a genuine value comparison -- logged as a failure signature, and a reason to keep the counterfactual-value (Boorman) and search-value (Kolling) terms architecturally separate.

## Confidence reasoning

Strong human fMRI from the Rushworth lab with a clean dissociation; source_quality 0.88. Held to 0.71 overall because mapping_fidelity is moderate (loop partner, not the frontopolar node) and the difficulty-confound debate is unresolved. Raises MECH-264 and SD-046 literature confidence; promotes nothing (both candidate / v4).
