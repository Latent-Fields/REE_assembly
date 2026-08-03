# Understanding Deep Learning Requires Rethinking Generalization (Zhang et al., ICLR 2017)

**Claim under test:** MECH-472 -- held-out context distinguishes skill acquisition from task memorisation; promote a competence update to durable only on evidence from contexts that did not generate it.

## What the paper did

Zhang, Bengio, Hardt, Recht and Vinyals ran a deliberately destructive experiment. They took standard image-classification networks and trained them not on real labels but on **randomly permuted labels**, and in a further variant on **random-noise pixels**. If the network's low training error meant it had learned the structure of the task, corrupting the labels should make training fail. It did not. The networks drove training error to zero regardless, with test accuracy at chance. Training time increased only by a small constant factor relative to true labels.

## Key findings relevant to the claim

The result establishes the strongest possible version of MECH-472's founding premise: **fitting the training distribution carries essentially no information about whether a task was understood.** A learner with enough capacity can reach perfect in-context performance by pure memorisation, with zero generalisable content. The authors also showed that explicit regularisation (weight decay, dropout) is neither necessary nor sufficient to obtain a small test error -- so one cannot even infer genuine acquisition from the machinery normally taken to prevent overfitting. The only reliable signal is performance on data the model was not fit to.

## How this translates to REE

MECH-472 wants to gate promotion-to-durable on held-out evidence precisely because in-context success can be counterfeit. Zhang et al. are the canonical proof that it *can* be counterfeit in the limit: a model that has memorised random labels looks perfect on its training set and knows nothing. For REE, this is the theoretical floor under the claim -- it says the danger MECH-472 guards against is real and can be arbitrarily severe, not a marginal effect.

The honest limit on the mapping, and the reason confidence sits at 0.7, is the level of abstraction. This is supervised classification with held-out *samples from the same distribution*, not an agent evaluated on held-out *contexts or tasks*. MECH-472's construct is stronger than an i.i.d. train/test split: it asks for evidence from a context that did not generate the competence, which is closer to distribution shift than to a random held-out sample. So Zhang et al. cleanly support the general claim "training fit does not certify acquisition" but do not themselves instantiate the held-out-context evaluation MECH-472 specifies. Read alongside Cobbe et al. (2019), which supplies the agentic/context version, this paper supplies the underlying dissociation in its purest form.

## Confidence reasoning

Source quality is very high -- an ICLR best paper that reframed a subfield and has been reproduced many times. But for a methodological claim like MECH-472 the load-bearing component is mapping fidelity, and here the setting is one abstraction up from REE's competence-promotion problem (supervised, sample-level, no reward or sequential control). Transfer risk reflects both the supervised-to-agentic jump and the sample-to-context jump. Hence a solid but not top-band confidence.
