# Meyer, Odriozola, Cohodes et al. 2019 — Ventral hippocampus interacts with prelimbic cortex during inhibition of threat response via learned safety in both mice and humans

## What the paper did

Meyer's group ran parallel mouse and human conditioned-inhibition paradigms — where a safety cue is presented in compound with a threat cue and the question is whether the safety cue inhibits the threat response. In mice they used projection-defined chemogenetics to manipulate ventral hippocampal (vHipp) neurons targeting either the prelimbic cortex (PL), the infralimbic cortex (IL), or the basolateral amygdala (BLA). In humans they used fMRI functional connectivity during the same task structure.

## Key finding

The vHipp neurons projecting to PL (and only those — not the IL- or BLA-projecting populations) showed the predicted pattern: more active during safety and compound cues than during threat cues, and activity correlated with the rodent's freezing behaviour. Activating this pathway altered the inhibition of threat by safety. In humans, hippocampal-to-dorsal-anterior-cingulate functional connectivity (but not hippocampal-to-vmPFC or hippocampal-to-BLA) differentiated threat, safety, and compound conditions in the same task.

The cross-species convergence is the strongest part of the result. Two different methods, two different species, and the same target-specific pathway emerges as the carrier of the safety-cue prediction signal.

## How it translates to REE

This entry sits next to Kreutzmann 2020 (IL-required-for-safety-expression) as the second piece of evidence that the predictive encoding of safety has its own substrate, parallel to both the threat (amygdalar) and the relief-completion (ventral-striatal) circuits. The vHipp-to-PL pathway is doing something the BA-to-NAc-shell pathway is not, and that something is specifically the *predictive* encoding of "this cue means safety / threat-absence."

For the REE architectural question, this reinforces the hybrid recommendation. Model 1 wins for the relief-completion event (Andreatta 2012, Navratilova 2012, Ramirez 2015 — all reward-circuit territory). Model 2 wins for the predictive encoding of safety cues (Kreutzmann 2020 IL, Meyer 2019 vHipp-PL — a separate prefrontal-hippocampal circuit). REE should therefore plan for two coordinated mechanisms:

- A relief-completion MECH that reuses goal-achievement infrastructure (MECH-057a beta-gate-drop, MECH-091 phase-reset, MECH-094 categorical write gate), with the polarity of the reinforcement set at the input as suffering-derivative-crosses-threshold.
- A separate safety-cue-prediction MECH that learns "this stimulus / this context predicts that suffering will not happen / will be reduced" as its own predictive structure, behaviourally analogous to "things liked" but anatomically and functionally separate. This second mechanism is what gates the agent's commitment-release decision (Is this context safe enough to drop the avoidance commitment?) rather than what consolidates the just-now-occurred relief event.

## Limitations and caveats

The species mapping is imperfect. In mice, the carrying pathway is vHipp-to-PL. In humans, the equivalent functional-connectivity pattern is hippocampus-to-dorsal-ACC, not hippocampus-to-PL or hippocampus-to-vmPFC. The authors translate this via cross-species homology, but PL/dACC homology is itself debated. The convergent *dissociation* across species (this pathway, not those other pathways, carries the safety signal) is the load-bearing finding rather than the literal anatomy.

The conditioned-inhibition paradigm is one specific operationalisation of safety-cue prediction, and the time-scales involved are short (seconds-to-minutes Pavlovian conditioning). Whether the same circuit handles the longer-horizon safety prediction that an REE goal-pursuit substrate would need to model is a transfer assumption — supported by the broader extinction-and-renewal literature, but not directly tested here.

## Confidence

Source quality is high (PNAS, cross-species, projection-defined manipulation in the rodent arm). Mapping fidelity is moderate because of the imperfect species homology and the paradigm specificity. Transfer risk is reduced by the species convergence. Net confidence 0.78, weakens — same role as Kreutzmann 2020, pulling the recommendation toward hybrid by surfacing the parallel substrate for safety-cue prediction.
