# Wanting/Liking Dissociation -- Berridge and Robinson (1998)

## What the paper does

Berridge and Robinson's canonical review establishes the experimental basis for distinguishing incentive salience (wanting) from hedonic pleasure (liking) in the reward system. Using dopamine-depleted rats, they show that animals with near-complete dopamine loss retain normal affective responses to sucrose (lip-licking, tongue protrusions) and normal aversive reactions to quinine (gaping), can still learn new hedonic associations, and can still have their hedonic responses pharmacologically enhanced -- but show profound apathy, akinesia, and failure to approach or work for food despite intact pleasure. The dissociation is also supported by human neurological and pharmacological data.

## Key findings relevant to REE

The dissociation has two components directly relevant to REE's infant stage design. First, positive hedonic reactions ('liking' responses) are present from the first postnatal day in human infants -- the newborn lip-lick to sweet taste is functionally equivalent to the rat taste-reactivity profile. This means the hedonic substrate is operational very early. Second, dopamine mediates approach motivation (wanting) independently of pleasure: it is possible to want without liking, and to like without wanting. The paper also notes that sucrose sweet taste 'liking' reactions appear at birth, with no learning required -- these are innate hedonic fixed-action patterns.

For the infant stage substrate, this implies that benefit contacts should generate a wanting-type signal (approach motivation, goal seeding) independently of whether the agent has a well-calibrated liking signal. The accidental contact with a beneficial resource in the grid-world would trigger approach repetition (wanting) even if the consummatory value (liking) is not yet precisely calibrated.

## How this maps to REE

REE's SD-014 distinguishes VALENCE_WANTING from VALENCE_LIKING as separate channels. Berridge and Robinson provide the mechanistic grounding for this architectural choice. MECH-189 (benefit contacts seed goal anchors) maps onto the wanting channel specifically: it is the dopamine-mediated wanting that drives the infant to approach and repeat the action that produced the benefit, not necessarily the accurate consummatory reward assessment. For the infant substrate design, this means the wanting channel should be responsive to novel benefit contacts earlier and more broadly than the liking channel -- and that the liking channel calibration can be a later-stage process.

The paper also provides the critical architectural prediction that wanting and liking can dissociate pathologically: if the wanting channel is hyperactivated (e.g., by a curriculum that produces high approach rates but low consummatory value calibration), the agent could develop incentive salience to goals that do not actually provide benefit. This is a risk for the infant substrate design if the exploration epoch is too reward-dense.

## Limitations and caveats

This is an adult rodent paper with human correlates; the developmental trajectory of the wanting/liking dissociation in infants is not directly addressed. While liking reactions are present at birth, whether the wanting system (mesolimbic dopamine) is independently functional in the first postnatal months is a separate question not resolved here. The pharmacological manipulation (6-OHDA dopamine depletion) is far more extreme than any developmental substrate manipulation REE would perform.

## Confidence reasoning

Confidence 0.72 reflects very high source quality (canonical highly-cited review, replicated extensively) with moderate mapping fidelity (the wanting/liking distinction maps well to SD-014, but the developmental infant application requires theoretical transfer) and moderate transfer risk (adult rodent pharmacology to infant learning substrate).
