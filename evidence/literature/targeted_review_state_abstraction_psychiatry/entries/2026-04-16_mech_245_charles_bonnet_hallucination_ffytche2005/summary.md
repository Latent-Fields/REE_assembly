# Visual Hallucinations and the Charles Bonnet Syndrome

**Ffytche DH (2005). Current Psychiatry Reports, 7(3):168-79. DOI: 10.1007/s11920-005-0050-3. PMID: 15935130.**

## What the paper did

Ffytche reviews the phenomenology and neurobiology of Charles Bonnet syndrome (CBS): complex visual hallucinations occurring in patients with visual impairment due to eye disease, with fully preserved insight and no psychosis. The paper resolves a longstanding definitional confusion in the CBS literature by arguing for two distinct hallucination syndromes within the CBS label. The first -- the "pure" CBS -- is directly linked to visual pathway pathology: loss of afferent input from the retina or optic pathway releases spontaneous activity in visual cortical areas, producing hallucinations whose content is predicted by which visual area is disinhibited (e.g., face hallucinations from fusiform face area disinhibition). The second subtype is linked to brainstem or ascending neurotransmitter pathway pathology and has a different phenomenological profile (more complex, narrative-like content, less modality-specific). The deafferentation subtype is the critical model for MECH-245.

## Key findings relevant to MECH-245

The defining feature of CBS is the preservation of insight: patients know their visual experiences are not real. This is not a failure of reality monitoring (which would be a MECH-094 or MECH-244 failure) but a failure of bottom-up sensory grounding. The visual cortex is generating predictions as part of its normal generative function, but without the afferent error signal that would normally anchor those predictions to actual visual input. The predictions propagate forward and are experienced as percepts -- but the patient's meta-cognitive system (which has intact information about their eye disease and intact general cognitive function) correctly identifies them as generated rather than received. This clinical picture is mechanistically informative: hallucination can occur without any impairment of the precision weighting or belief-updating systems that MECH-244 requires.

Ffytche also proposes the thalamocortical burst-firing mechanism: deafferentation shifts thalamocortical circuits from tonic to burst firing mode, which releases cortical areas from the tonic inhibition that normally suppresses spontaneous activity. Visual cortex, deprived of retinal drive, begins generating spontaneous activity that propagates as if it were a sensory signal.

## REE mapping

MECH-245 requires a mechanism where top-down E1 generative predictions propagate as percepts without corresponding bottom-up sensory grounding. CBS provides the cleanest available demonstration: when sensory input is removed, the generative model runs forward without a corrective error signal, and its outputs are experienced as real percepts. In the REE architecture, E1's predictive top-down signals would normally be continuously corrected by the sensory prediction error; when that correction is absent (bottom-up pathway damaged or suppressed), E1's predictions propagate as if sensory in origin and influence phi(z) accordingly. Critically, this is mechanistically independent of MECH-244: in CBS, the world model is not self-sealing (the patient correctly reports that the experiences are hallucinations), and precision weighting is intact. What is absent is the bottom-up sensory anchor.

This makes CBS an important clinical dissociation for the REE framework: it demonstrates that you can have pure generative-model dominance (MECH-245) without precision-weighting failure (MECH-244), and without write-gate failure (MECH-094 -- the experiences are correctly tagged as non-real by the meta-cognitive system). The three failure modes are separable, and CBS is evidence that at least one of them (MECH-245) can occur in isolation.

## Limitations and caveats

CBS is a visual-modality, non-psychotic population phenomenon. The most clinically significant hallucinations in psychiatry are auditory verbal hallucinations (AVHs) in psychosis, where insight is typically absent and precision weighting is also dysregulated. Whether AVHs in schizophrenia involve the same deafferentation-like mechanism (E1 generating predictions without bottom-up correction) is plausible but requires separate evidence. The presence of preserved insight in CBS and its absence in psychotic hallucinations may reflect the simultaneous presence of MECH-244 in the latter -- precision failure prevents the meta-cognitive system from correctly tagging the hallucinations as generated. This would mean psychotic AVHs involve a compound of MECH-245 (generative dominance) and MECH-244 (precision failure suppressing insight), which is clinically consistent but not directly tested here.

## Confidence reasoning

Confidence 0.78. CBS provides the best available clinical isolation of MECH-245 from MECH-244 and MECH-094. The deafferentation mechanism maps directly onto the generative dominance claim. The primary caveat is modality specificity: visual deafferentation in a non-psychotic population may not directly generalise to auditory hallucinations in psychosis, where the MECH-244/245 distinction is most clinically urgent.
