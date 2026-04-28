# Burgess et al. 2013 -- Amygdala lesions reduce cataplexy in orexin knock-out mice

**Source:** *J Neurosci* 33(23):9734-42. DOI: [10.1523/JNEUROSCI.5632-12.2013](https://doi.org/10.1523/JNEUROSCI.5632-12.2013) (PMID 23739970, PMC3704329).
**Cited via PubMed.**

## What the paper did

Burgess and colleagues asked a sharp question: when an orexin-deficient animal undergoes cataplexy -- the sudden loss of postural muscle tone triggered by emotionally salient stimuli -- which structure converts the emotional trigger into the motor failure? They combined anterograde and retrograde tract-tracing in mice to chart the central nucleus of the amygdala's (CeA) outputs to brainstem motor-tone nuclei, and then performed bilateral excitotoxic lesions of the amygdala in orexin-KO mice while measuring cataplexy under two emotional-trigger paradigms (running wheel, chocolate access). The behavioural readout is straightforward: rate and number of cataplexy bouts per unit time, with sleep-wake architecture as a control.

## Key findings

The tracing yielded a clean projection picture: CeA GABAergic neurons heavily innervate the ventrolateral periaqueductal gray, lateral pontine tegmentum, locus coeruleus, and dorsal raphe -- exactly the brainstem nuclei that maintain waking muscle tone. The behavioural result is the punchline: bilateral amygdala lesions markedly reduced emotion-triggered cataplexy in orexin-KO mice, and the reduction was specific to emotionally-elicited bouts. Spontaneous (non-elicited) bouts also fell, but baseline sleep-wake architecture was preserved -- the lesion did not turn the animals into quiescent sleepers, it broke the emotion-to-atonia coupling.

## How this maps to MECH-281

MECH-281 commits to a specific claim: an orexin-analog gain modulator gates the coupling between drive/emotional state and motor activation, and BLA/CeA arbitration is one canonical downstream target. Loss of this gain produces a motor-coupling failure where z_harm and drive_level compute normally, but action selection fails to integrate them. Burgess provides the cleanest available mechanistic substrate for that statement. In orexin loss, the CeA -> brainstem-motor-tone path becomes the dominant route through which emotional state translates into motor failure; remove the amygdala, and the failure does not happen even though the orexin loss is unchanged. The REE translation is direct: SD-037's override_signal reweights amygdala arbitration in the commit-gate threshold; at override_signal = 0, amygdala-driven inhibition of motor activation dominates and we see the cataplexy-analog. Burgess is what makes that prediction biologically grounded rather than borrowed-by-analogy.

## Limitations and caveats

Two honest caveats. First, cataplexy is REM-atonia intrusion -- a specific motor failure mode -- whereas MECH-281's broader formulation covers any failure of drive/emotion to recruit motor activation (depressive psychomotor retardation, freeze-after-trauma, etc.). Burgess speaks directly to the narcolepsy axis; whether the same CeA -> brainstem path handles the other failure modes is suggestive but not shown here. Second, this is rodent and species-specific -- the emotional triggers (chocolate, running wheel) are not the human laughter trigger, and the rodent cataplexy phenotype differs from human cataplexy in duration and presentation. The mechanism transfer is well-supported in the broader narcolepsy literature, but it should be flagged.

## Confidence reasoning

I assign 0.85. Source quality is high (J Neurosci, well-cited Scammell lab, replicated in subsequent work). Mapping fidelity to the canonical motor-coupling axis is high (this is precisely the lesion experiment MECH-281's prediction asks for). Transfer risk is the chain mouse -> primate -> generic REE coupling claim, and that risk is real but moderate given the broader narcolepsy literature converges. The number sits below 0.9 because the paper does not directly speak to the non-atonia motor-coupling failures the broader MECH-281 phrasing covers.
