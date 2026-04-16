# Sigurdsson et al. 2010 — Impaired Hippocampal-Prefrontal Synchrony and Goal Navigation Failure

**Nature 464:763-767 | doi: 10.1038/nature08855 | PMID: 20360742**

## What the paper did

Sigurdsson and colleagues used a genetic mouse model of schizophrenia risk -- Df(16)A+/- mice carrying a heterozygous deletion of the 22q11.2 chromosomal region, one of the largest single known genetic risk factors for schizophrenia -- to ask whether reduced hippocampal-prefrontal synchrony has causal consequences for goal-directed navigation. They recorded LFPs and single units simultaneously from hippocampal CA1 and medial PFC while mice learned a spatial working memory T-maze task over multiple days, comparing mutant and wild-type animals. The critical design feature is that the genetic manipulation provides a causal lever: if theta coherence is impaired and goal navigation is impaired in the same animals, and the coherence predicts the navigation trajectory, this goes beyond correlation.

## Key findings relevant to ARC-032

Df(16)A+/- mice showed dramatically reduced theta coherence between hippocampus and mPFC compared to wild-type controls, and this reduction was observable from the beginning of training. Crucially, pre-training theta coherence was a predictor of task acquisition rate: mice with lower initial coherence took significantly more days to reach criterion. Prefrontal unit phase-locking to hippocampal theta was also impaired in the mutants. The functional consequence is straightforward -- the animals with degraded theta coupling between frontal and hippocampal structures were slower to learn goal-directed navigation, and in the most severely affected mice the deficit persisted throughout the training period.

## Translation to REE

This paper provides the clearest disruption evidence for ARC-032. The claim is not just that theta coupling is present during goal-directed navigation (shown by Hyman, Benchenane, and Jones & Wilson), but that the theta channel is the *primary pathway* through which frontal goal context reaches hippocampal navigation. Sigurdsson et al. operationalise the disruption prediction: ablate or degrade the theta synchrony channel and goal navigation degrades proportionally. In REE architecture terms, this is what a ThetaBuffer lesion would look like -- E1 goal context cannot reach E3 at the theta rate, so E3's trajectory scoring cannot be properly conditioned on the current goal, and navigation becomes less reliably goal-directed. The fact that pre-training coherence predicts learning rate (rather than just correlating with performance within trials) suggests the theta channel is a structural prerequisite for the frontal-hippocampal goal pathway, not merely a correlate of successful navigation.

## Limitations and caveats

The Df(16)A+/- model is a model of schizophrenia-related circuit pathology, not a targeted manipulation of the theta channel specifically. The deletion affects multiple genes and could produce circuit changes beyond the theta synchrony disruption (e.g., GABA interneuron deficits, dopaminergic changes) that contribute to the navigation impairment through routes other than the frontal-hippocampal theta channel. The study demonstrates that theta synchrony is lower in the impaired animals but cannot cleanly isolate theta coupling as the causal bottleneck versus other circuit changes that co-occur with the deletion. Additionally, the task tests acquisition of goal-directed behaviour over days, whereas ARC-032 describes a real-time goal-context delivery mechanism operating at the theta cycle timescale -- the two timescales of analysis are different.

## Confidence reasoning

Confidence 0.77. The paper provides strong causal-correlational evidence that theta channel integrity is necessary for goal navigation competence -- the strongest disruption evidence available in the literature for this claim. The deductions are primarily for the pathological model confound and the acquisition-vs-maintenance timescale mismatch. The Nature venue and causal genetic design are significant positive factors. This entry fills the disruption angle specifically requested in the lit-pull: what happens when frontal-hippocampal theta synchrony is broken.
