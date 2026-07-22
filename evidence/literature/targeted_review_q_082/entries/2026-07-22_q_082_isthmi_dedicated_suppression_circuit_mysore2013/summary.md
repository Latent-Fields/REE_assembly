# Mysore & Knudsen (2013) -- A shared inhibitory circuit for both exogenous and endogenous control of stimulus selection

## What the paper did

Working in the barn owl midbrain, the authors targeted the nucleus isthmi pars magnocellularis (Imc), an inhibitory nucleus reciprocally connected with the optic tectum -- the avian homologue of the superior colliculus. They recorded single units in the tectum while stimuli competed for representation, and they reversibly inactivated Imc focally to test whether it was causally necessary for that competition.

## Key findings relevant to Q-082

Inactivating Imc abolished competitive interactions in the tectum. Not attenuated -- abolished. And it did so for both stimulus-driven competition, where a salient distractor competes with a target on bottom-up grounds, and internally driven competition, where an endogenous signal biases which stimulus wins. Imc neurons take spatially precise multisensory and endogenous input and convert it into powerful inhibitory output that suppresses competing representations across the entire tectal space map. The authors present this as a neural mechanism for constructing a priority map.

## How this translates to Q-082

Q-082 asks whether REE requires an explicit pre-selection suppression substrate, or whether existing precision-weighted cue routing plus the MECH-254 top-k boundary bottleneck already suffice. This paper is the strongest affirmative evidence I found for the first horn. It shows that at least one nervous system solves the selection problem with a dedicated, anatomically separable inhibitory circuit that acts *before* any representation acquires behavioural control, and that this circuit is shared between the exogenous and endogenous routes rather than duplicated.

Two details are worth carrying forward beyond the headline. First, the failure mode under inactivation was total loss of competitive selection, not graceful degradation into a facilitation-only regime -- which would predict, if the analogy holds, that a priority map lacking an inhibitory partner does not merely select worse under competition but fails to select. Second, the suppression was global across the space map from a spatially precise input. A pairwise or locally scoped inhibition scheme would not reproduce that, so if REE ever did build this, the naive local implementation is the wrong one.

## Limitations and confidence

The transfer is the honest problem, and it is larger here than in most entries I write. This is a retinotopic spatial space map in an avian midbrain, solving an explicitly spatial competition problem. REE's precision-weighted cue routing is not spatial, and the MECH-254 top-k boundary bottleneck is a capacity constraint rather than a map with neighbourhoods. "Suppression across the entire space map" has no clean structural counterpart in REE. The mammalian homologue of Imc, the parabigeminal nucleus, is considerably less well characterised functionally than the avian circuit, so this is not a case where I can lean on a closer preparation.

More importantly for governance: this paper establishes that biology *has* such a substrate. It says nothing about whether REE *needs* one, because it never tests an architecture like REE's. Whether the top-k bottleneck already discharges this function is exactly the question, and it is answered by MECH-467 leg 3 plus ablation of REE's existing mechanisms -- not by literature and not by a probe of its own. Q-082 is registered as a gated open question with an explicit do-not-build and do-not-queue instruction, and nothing in this entry changes that. This is grounding for the question, not movement toward an answer.

Confidence 0.74.

*Retrieved via PubMed. [DOI](https://doi.org/10.1038/nn.3352)*
