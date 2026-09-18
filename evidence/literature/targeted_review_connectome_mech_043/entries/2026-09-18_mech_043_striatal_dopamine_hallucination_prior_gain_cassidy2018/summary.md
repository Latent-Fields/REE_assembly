# A Perceptual Inference Mechanism for Hallucinations Linked to Striatal Dopamine

Cassidy, Balsam, Weinstein, Rosengard, Slifstein, Daw, Abi-Dargham & Horga (2018), *Current Biology* 28(4):503-514.e4. DOI [10.1016/j.cub.2017.12.059](https://doi.org/10.1016/j.cub.2017.12.059) · PMID 29398218 · PMC5820222

**Claim tested:** MECH-043 — *Dopamine-like modulation of precision-weighting for unsigned prediction errors.*
**Direction:** supports (confidence 0.78)

## What the paper did

The question is an old one asked well: hallucinations are known to depend on excessive striatal dopamine, but what is the cognitive step in between? The authors built a task measuring illusory shifts in the perceived duration of auditory stimuli under parametrically varied uncertainty — a psychophysical readout of how much weight a listener places on prior expectation when the evidence is poor. They then studied unmedicated patients with schizophrenia varying in hallucination severity, plus healthy individuals under an amphetamine challenge, with PET imaging of striatal dopamine release and structural MRI.

Three findings stack into an unusually complete causal chain. Hallucination severity correlated with the perceptual bias — disproportionate gain on expectations under uncertainty. The same bias could be *pharmacologically induced* in healthy people by amphetamine, so this is not merely a correlation in patients. And the magnitude of that induction correlated strongly with directly measured striatal dopamine release, with the bias further related to dorsal anterior cingulate cortical volume.

## How this translates to REE

MECH-043's CONFIRMING condition has two halves. The mechanistic half — that the precision term is computed from unsigned error magnitude, live-invoked, and actually influences commitment — is addressed by Haarsma et al. (2021) and by INV-008's internal audit. This paper is the best available evidence for the *behavioural* half: that misallocating a dopamine-dependent gain produces a measurable shift in a hallucination-like dependent variable.

Its value to REE is as much methodological as evidential. It shows what a hallucination-like DV can concretely look like in an agent that has no verbal report: a signed perceptual displacement toward the prior, measured under uncertainty that the experimenter varies parametrically. That is a design REE can actually instantiate, and MECH-043's CONFIRMING condition asks for precisely such a sweep. There is a second, narrower point of contact: REE feeds `current_precision` into the dACC affective-PE weighting as well as the E3 commitment gate, and this paper independently implicates dACC in tracking the uncertainty the gain is applied under.

## Limitations and caveats

There is an inversion here that I do not want to paper over, because getting it backwards would waste an experiment.

In a precision-weighting scheme, excessive weight on priors and excessive precision on sensory prediction errors are *opposite* dispositions. The first ignores the incoming evidence; the second over-attends to it. Cassidy et al. manipulate the prior side. REE's `current_precision = 1/(running_variance + 1e-6)` sits on the error side. Mapping this paper onto MECH-043 therefore runs through an assumed reciprocity — low precision on the error term equals high relative weight on the prior — which holds in an idealised two-sided Bayesian balance but is not guaranteed in REE's implementation, where `running_variance` is a self-estimated EMA rather than a normalised term in such a balance.

The practical consequence is directional, and it is the most useful thing this entry carries. On this paper's logic, the hallucination-like shift should appear when REE's precision channel is *down*-weighted or mis-scaled relative to the prior, not when it is simply raised. A sweep that only increases precision may look for the effect in the wrong direction and record a spurious null — which would read as MECH-043 falsifier (iii) when it was in fact a design error. Any sweep should therefore be two-sided.

Two further limits. Amphetamine is a non-selective monoamine releaser, raising noradrenaline and serotonin alongside dopamine; attribution to dopamine rests on the correlation with PET-measured striatal displacement rather than on pharmacological selectivity, so this study does not on its own exclude falsifier (iv), a shared precision-scale parameter that is not dopamine-specific. And the sample sizes are modest by pharmacological-imaging standards, as they almost always are when the participants must be unmedicated.
