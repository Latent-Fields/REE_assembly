# Dissociation of reward anticipation and outcome with event-related fMRI (Knutson 2001b)

## What the paper did

Same Knutson lab, same MID paradigm, n=9 healthy volunteers, but with the contrast structure designed to dissociate anticipation (cue presented) from outcome (reward delivered). Multiple regression analyses partitioned BOLD variance attributable to each event type within the same trials.

## Key findings relevant to the SD-014 question

The headline result: anticipation of reward activates the ventral striatum (centred on NAcc); outcome of reward activates the ventromedial frontal cortex (vmPFC). Both regions sit along the dopaminergic projection trajectory but are anatomically distinct. The conclusion is that "reward anticipation and outcomes may differentially recruit distinct regions". Anticipation is one neural construct; outcome is another.

For REE this is direct architectural evidence that the wanting/liking dissociation Berridge laid out at the substrate level (NAc shell hedonic hotspot vs VTA-NAc-prefrontal wanting circuit) extends to a third construct: anticipatory positive affect at the cue, anatomically distinct from both. The vmPFC outcome signal maps cleanly onto VALENCE_LIKING (consummatory hedonic at receipt). The ventral striatum / NAcc anticipation signal is the candidate VALENCE_EXCITEMENT — a representation of *the cue is signalling something good will happen*, distinct from *I am moving toward the goal* (wanting) and *I am receiving the goal* (liking).

## How this maps to REE

REE's residue field already records VALENCE_LIKING at z_goal locations on contact (the consummatory write). It records VALENCE_WANTING at the same locations during update. What it does not record is anticipatory-positive-affect — the moment the agent encounters a cue that *predicts* an upcoming positive outcome. That signal exists in MECH-216 schema readout but does not write to the residue field as a distinct affective dimension. Adding VALENCE_EXCITEMENT as a 5th channel would close this gap.

The architectural payoff: replay prioritisation (MECH-205 surprise-gated replay) and ghost-goal scoring (MECH-292 ghost_priority) could both consume VALENCE_EXCITEMENT to weight locations where positive-anticipation has been recorded. Currently they consume VALENCE_WANTING and staleness; an excitement term would specifically prioritise *cue-rich* locations over *goal-rich-but-already-explored* locations.

## Limitations and caveats

Smaller n than the foundational 2001a; both papers are early-MID-paradigm work that established the framework but had limited statistical power individually. The anatomical dissociation depends on fMRI spatial resolution and is sensitive to smoothing kernel size (cf. Sacchet & Knutson 2012). The vmPFC-outcome / NAcc-anticipation pattern is robust at the meta-analytic level but individual studies vary.

## Confidence reasoning

0.78. Direct architectural support for the 5th channel proposal; lower than 2001a's 0.85 because of smaller n and slightly indirect mapping (the paper does not measure happiness directly, only the BOLD dissociation). Combined with 2001a, the joint reading is strong.

Source: PubMed via PMID 11726774. [DOI](https://doi.org/10.1097/00001756-200112040-00016).
