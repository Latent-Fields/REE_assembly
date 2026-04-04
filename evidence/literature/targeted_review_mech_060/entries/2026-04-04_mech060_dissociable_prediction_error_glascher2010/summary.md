# Literature Summary: 2026-04-04_mech060_dissociable_prediction_error_glascher2010

## Claims Tested

- `MECH-060`

## Source

- Glascher J, Daw N, Dayan P, O'Doherty JP (2010), *States versus Rewards: Dissociable Neural Prediction Error Signals Underlying Model-Based and Model-Free Reinforcement Learning*. Neuron 66: 585-595.
- DOI: 10.1016/j.neuron.2010.04.016
- URL: https://pubmed.ncbi.nlm.nih.gov/20510862/

## Mapping to REE

MECH-060 requires that pre-commit simulation error and post-commit realized error stay responsibility-distinct via write-boundary enforcement. The core empirical question is whether distinct error channels are biologically real and architecturally separable -- or whether they are a modelling convenience that collapses in practice.

Glascher et al. (2010) provides the clearest empirical grounding for the two-channel view. Using fMRI with a probabilistic Markov decision task, they identify two dissociable prediction error signals: a state prediction error (SPE) localised to intraparietal sulcus and lateral prefrontal cortex, and a reward prediction error (RPE) localised to ventral striatum. The SPE indexes discrepancies between the agent's current model and observed state transitions -- this is prospective, model-based, and arises before outcome delivery. The RPE indexes actual reward minus expectation -- this is retrospective, realized-outcome-based, and arises at outcome receipt.

The REE mapping is direct. The SPE corresponds to the pre-commit simulation channel: E2 computes expected harm across candidate trajectories before any action commits (before env.step). The RPE corresponds to the post-commit realized-error channel: harm returned by the environment post-action updates the residue field. Glascher et al.'s data show these are anatomically separated in the brain -- the intraparietal sulcus/lateral PFC complex does not co-localise with ventral striatum -- providing biological precedent for the architectural separation REE enforces by design.

The paper does not address write-boundary enforcement or what happens when channels are contaminated. Its contribution is establishing biological plausibility for the two-channel separation, not demonstrating that mixing the channels is harmful. The MECH-060 EXQ-005 experiment (write_locus_contamination) provides the contamination-consequence evidence that this paper cannot.

## Caveats and Mapping Limits

- The SPE/RPE dissociation is within model-based RL; the mapping to REE's pre/post-commit boundary requires the additional step of identifying model-based planning with pre-commit simulation.
- The paper's SPE and RPE both contribute to behavior at output; they are not write-separated in the sense that MECH-060 requires. The distinction is computational origin, not write locus.
- Confidence capped at 0.72 because the write-boundary enforcement aspect of MECH-060 is not directly tested.

## Direction and Confidence

- `evidence_direction`: `supports`
- `confidence`: `0.72`
- Rationale: strong biological precedent for dissociable pre-outcome (simulational) and post-outcome (realized) error channels; does not test write-boundary contamination consequences.
