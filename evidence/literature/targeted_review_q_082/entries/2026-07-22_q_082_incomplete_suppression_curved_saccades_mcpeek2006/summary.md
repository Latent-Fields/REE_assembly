# McPeek (2006) -- Incomplete suppression of distractor-related activity in the frontal eye field results in curved saccades

## What the paper did

Saccades made in the presence of distractors do not travel straight; they bow toward or away from the distractor. McPeek recorded frontal eye field neurons during visual search while classifying saccades as curved or straight, and then -- the step that makes the paper causal rather than correlational -- applied subthreshold microstimulation to FEF sites, patterned to resemble the activity recorded on curved-saccade trials, during saccades to targets presented without any distractor at all.

## Key findings relevant to Q-082

Saccades curving toward a distractor were accompanied by elevated perisaccadic activity in neurons coding the distractor's location; saccades curving away were accompanied by reduced activity there. Activity in target-coding neurons did not differ between curved and straight saccades. The microstimulation induced curvature toward the stimulated location in the absence of a real distractor. Taken together: curvature is caused by residual, incompletely suppressed distractor activity at the moment the movement is committed.

## How this translates to Q-082

I filed Mysore & Knudsen as the affirmative case for Q-082 and this is the counterweight, which is why the directory holds both. Here suppression is not a distinct upstream gate. It is the graded competitive dynamics of the selection map itself, and target-coding activity is untouched -- the whole effect lives in how far the distractor's representation has been pushed down by the time the system commits. That is much closer to what REE already has. Precision-weighted cue routing plus the MECH-254 top-k boundary bottleneck is a competition-within-a-map architecture, and on this paper's reading that is the substrate where suppression happens, not something that needs a suppression module bolted on before it.

The finding that reframes the question most usefully is that commitment can occur before competition resolves. The system does not wait for a clean winner; it emits, and whatever competition remains unresolved contaminates what comes out. Translated to REE, the interesting failure mode is not "a distractor was never suppressed" but "the top-k boundary committed while the competition was still live and the selection carried contamination". That is a different diagnostic than a missing-substrate diagnostic, and it is checkable against mechanisms REE already has.

## Limitations and confidence

The readout is trajectory curvature, a continuous motor variable, and REE's committed actions are discrete. The specific signature -- suppression residue bleeding into the path of the movement -- has no REE counterpart, so the analogy has to be carried at the level of "unresolved competition contaminates the commitment" rather than at the level of the measurement. Whether a discrete commitment shows the same graded contamination is not something this paper can tell us. FEF is also one node among several in the selection network; the SC evidence and the FEF evidence are not interchangeable, and the paper itself is framed against a prior SC literature.

Confidence 0.66. This is good evidence, causally grounded, and its main value to Q-082 is that it makes the question genuinely two-sided rather than a foregone conclusion in favour of building something.

*Retrieved via PubMed. [DOI](https://doi.org/10.1152/jn.00564.2006)*
