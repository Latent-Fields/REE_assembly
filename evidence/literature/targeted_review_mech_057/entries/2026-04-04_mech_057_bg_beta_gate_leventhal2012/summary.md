# Literature Summary: 2026-04-04_mech_057_bg_beta_gate_leventhal2012

## Claims Tested

- `MECH-057a` (Committed action sequences suppress sensory precision reweighting until execution completes)

## Source

- Leventhal DK, Gage GJ, Schmidt R, Pettibone JR, Case AC, Berke JD (2012).
  *Basal Ganglia Beta Oscillations Accompany Cue Utilization.*
  Neuron, 73(3), 523-536. [DOI: 10.1016/j.neuron.2011.11.032](https://doi.org/10.1016/j.neuron.2011.11.032)
- PMID: 22325204 | PMC: PMC3463873

## What Was Studied

Leventhal et al. recorded local field potentials and single-unit activity across multiple cortical and basal ganglia (BG) regions in rats performing four variants of a cued choice task. They asked: when do beta oscillations (~20 Hz) rise and fall, and what cognitive or motor variable do they track?

## Key Findings

The result that matters for MECH-057a is not the obvious one. Beta power was not rigidly coupled to movement initiation, movement suppression, or cue onset alone. Instead, beta power was most reliably elevated *after* the cue had been used to determine a motor output -- that is, post-decision, when the circuit had stabilised around a committed course of action. The authors describe this as a "postdecision stabilised state" that reduces interference from alternative potential actions.

Beta phase was reset rapidly by salient cues, consistent with the gate opening transiently to allow sensory information to update the motor plan. But once the decision was made, beta rose -- and the inference is that the gate closes again, protecting the committed state from further sensory revision. In Parkinson's disease, the authors propose, this stabilisation becomes pathologically persistent: the gate never opens, producing akinesia.

## Mapping to MECH-057a

MECH-057a claims that committed action sequences suppress sensory precision reweighting until execution completes. Leventhal et al. provide the empirical description of the circuit event that would implement this: BG beta elevation accompanies the post-decision stabilised state. The claim that high beta = "closed gate" = reduced sensitivity to competing sensory signals maps directly onto the precision-suppression mechanism. This paper establishes the circuit-level correlate; Palmer et al. 2019 (see companion entry) provides the predictive-coding interpretation linking beta specifically to precision weighting rather than to error magnitude.

## Caveats

The paper does not directly measure sensory prediction error suppression or anything resembling precision weighting. The "reduced interference from alternative actions" framing is inferential -- derived from the task logic and beta timing, not from directly blocking a sensory channel and measuring the downstream effect. The step from "beta post-commitment" to "sensory precision suppressed during commitment" requires the additional mechanistic bridge that Palmer et al. supply.

## Direction and Confidence

- `evidence_direction`: `supports`
- `confidence`: `0.71`
- Rationale: Strong circuit-level correlate of commitment-phase gating; indirect link to sensory precision suppression specifically.
