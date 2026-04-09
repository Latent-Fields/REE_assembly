# Summary: Horing and Buchel (2022) -- The human insula processes both modality-independent and pain-selective learning signals

**Entry:** 2026-04-09_sd_020_insula_unsigned_pe_surprise_horing2022
**Claim tested:** SD-020
**Evidence direction:** supports

## What the study did

Horing and Buchel designed a cross-modal learning paradigm in which 47 healthy adults received two types of aversive stimuli -- painful heat and loud sounds -- at varying intensities, cued by visual stimuli that participants learned to associate with specific intensity levels. By varying both intensity and modality unpredictably, the paradigm allowed the authors to decompose insula fMRI responses into four components: unsigned intensity PE (modality-independent aversive surprise), signed intensity PE for pain (pain-specific), signed intensity PE for sound (sound-specific), and modality PE (surprise about which modality occurred). The paradigm was large by fMRI standards (N=47) and included skin conductance as a peripheral learning signal.

## Key findings

Anterior insula activity correlated with unsigned intensity PE irrespective of modality -- described by the authors as "an unspecific aversive surprise signal." This is the key finding for SD-020: anterior insula codes how surprising the aversive outcome was (unsigned PE), regardless of whether the aversive event was pain or a loud sound. Dorsal posterior insula, by contrast, encoded signed intensity PE specifically for pain but not sound -- a pain-dedicated signal. This within-study dissociation confirms both the anterior (unsigned, modality-independent PE) and posterior (pain-specific signed PE) profiles.

## REE translation

This is the strongest pre-Chen direct evidence for SD-020. The paper's own language -- "unspecific aversive surprise signal" for anterior insula -- is nearly a verbatim description of what SD-020 proposes for z_harm_a. The SD-020 redesign trains z_harm_a on how surprising the current harm level is, not how high it is; and that is exactly what anterior insula encodes here. There is one important complication for REE: the modality-independence finding means that AIC does not intrinsically distinguish harm-surprise from any-aversive-surprise. If z_harm_a maps onto AIC, harm-specificity must be enforced architecturally (e.g., by restricting the harm PE signal to harm-relevant contexts, or by gating via z_harm_s). SD-020 does not yet address this; it may be a refinement that needs documenting as a follow-on design question.

## Limitations and caveats

The modality-independence finding is conceptually important but also a potential concern for SD-020's specificity. An AIC that responds equally to harm-surprise and sound-surprise cannot on its own implement z_harm_a as a harm-specific signal. REE may require either: (a) assuming the experimental environment provides only harm as the relevant aversive modality, or (b) explicitly gating the PE training target by harm-relevant context. This limitation does not weaken support for the PE/surprise coding claim -- only for the assumption that AIC is already harm-specific without additional gating. Skin conductance as a PE proxy carries the same indirect measurement concern as in Geuter 2017.

## Confidence reasoning

Confidence 0.90 -- the highest of the four entries. Large sample (N=47), cross-modal design, Buchel lab, PLoS Biology, open access. The unsigned PE finding maps almost directly onto SD-020's training target claim. The main deduction from 1.0 is the modality-independence caveat (noted above), which introduces a nuance that SD-020 will need to address in implementation.
