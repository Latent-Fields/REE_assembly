# Wang, Wann, Yuan, Ramos Alvarez, Stead & Muzzio 2012 — Long-Term Stabilization of Place Cell Remapping by a Fearful Experience

**Source:** Journal of Neuroscience, [DOI 10.1523/JNEUROSCI.0480-12.2012](https://doi.org/10.1523/JNEUROSCI.0480-12.2012) (PubMed PMID 23136419). According to PubMed.

## What the paper did

The authors recorded the same hippocampal CA1 place cells in mice over multiple days of predator-odor contextual fear conditioning. The within-cell longitudinal design lets them ask not just whether fear remaps the map (Moita 2004 settled that), but whether the new representation persists.

## Key findings relevant to the SD-011 generalization

A subset of CA1 cells changed their preferred firing locations in response to the fearful stimulus, and — critically — the newly formed representations of the fearful context stabilized in the long term. This is the consolidation-into-the-map result. Once a context acquires fear/threat loading, the remapped place ensemble persists across days, not just across the within-episode arousal state.

## REE translation

This adds two architectural features to the SD-011 generalization picture:

1. *Persistence.* Affect-channel tagging on the hippocampal map is consolidated. It's not a transient firing-rate modulation that disappears when the animal calms down — it's a structural reorganization that survives and supports future episodic recall.
2. *Innate-threat pathway recruitment.* Predator-odor conditioning recruits innate-threat circuitry (PAG, central amygdala) that is partly distinct from the shock-pain circuitry of Moita 2004. The convergent finding across paradigms suggests fear/threat as a single map-tagged channel rather than multiple sub-channels — at least at the level of CA1 readout.

For V3/V4, this argues that affect-stream tagging on the hippocampal map should be implemented as a write-once-and-stabilize mechanism (consistent with sleep-replay consolidation and MECH-285) rather than as a perpetually-recomputed signal.

## Limitations and caveats

The "subset of cells" terminology hides the magnitude. The persistence is shown for days, not weeks or months — the very-long-term fate of the representation is not addressed. The predator-odor paradigm is one specific innate-threat condition; whether shock-based and predator-based fear converge on the *same* remapped representation or merely on the same *kind* of remapping is unaddressed.

## Confidence

0.80 — methodologically strong (cross-day recording is hard), converges with Moita 2004 across a different aversive paradigm, and adds the persistence claim. Bounded by sample size and the single-paradigm scope.
