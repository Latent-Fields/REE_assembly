# Action-Driven Contrastive Representation for Reinforcement Learning (ADAT)

**Kim, Lee & Kim (2022) -- PLOS ONE**

## What the paper did

ADAT extends the CURL framework by replacing the unsupervised augmentation-consistency objective with a supervised category-based contrastive objective. Instead of pulling two augmentations of the same observation together, ADAT pulls together observations that share the same action label. The hypothesis is that action-type categories are the functionally relevant categorical dimensions for an RL encoder serving a control policy: representations that cluster by action type will emphasise the features that cause the agent to take different actions while suppressing visual details that are irrelevant to control decisions. The authors introduced an Unbiased Sampling module to make ADAT compatible with off-policy RL algorithms, and evaluated it on Atari Games and OpenAI ProcGen, showing 1.24x mean human-normalised score improvement over CURL and state-of-the-art results on 15 of 26 Atari games at the 100k step benchmark.

## Key findings relevant to SD-009

The paper's key finding is that using category labels as the supervisory signal for contrastive auxiliary learning outperforms unsupervised contrastive learning (CURL). This directly advances the case for SD-009. Where CURL showed that any discriminative auxiliary objective improves encoder quality over RL signal alone, ADAT shows that the specific choice of categorical dimension matters: using labels that align with the encoder's downstream task (action selection for ADAT, harm evaluation for SD-009's z_world) produces better representations than using generic augmentation invariance. The information-theoretic logic is clear: a supervised categorical signal over task-relevant categories enforces exactly the latent structure the downstream computation needs, whereas unsupervised contrastive learning imposes a weaker and less targeted constraint.

For SD-009, this means the choice to use a supervised CE loss over event types (hazard present, absent, neutral) is better motivated than simply adding any auxiliary objective. The event-type categories are the relevant categorical dimension for z_world's downstream consumer (E3's harm evaluator), and the CE loss enforces exactly the latent structure that E3 needs: a geometry where hazard states are clearly separated from safe states in the z_world manifold. ADAT demonstrates empirically that this kind of category-supervision produces stronger improvements than unsupervised alternatives.

## Mapping to REE

SD-009 is ADAT's natural transposition from action-supervision to event-supervision. ADAT asks: what category should the encoder be organised around for action selection tasks? Answer: action type. SD-009 asks: what category should z_world's encoder be organised around for harm evaluation? Answer: event type (hazard present, absent, neutral). Both papers share the same structural claim -- that the appropriate auxiliary supervisory signal is the categorical dimension that matters for the downstream computation -- and differ only in what that categorical dimension is. This makes ADAT a closer analogue to SD-009 than CURL, and its superior performance over CURL provides additional support for the supervised-categorical design choice.

## Limitations and caveats

The categorical dimensions differ in an important way: action types are the agent's own choices, whereas event types are properties of the environment. This distinction matters for the information-theoretic argument. ADAT's encoding produces action-aligned representations, which are useful for planning what to do. SD-009's CE loss produces event-aligned representations, which are useful for evaluating what the environment contains. These are complementary rather than identical goals. A further caveat is that ADAT's evaluation is on high-dimensional visual observation spaces (Atari pixels), while REE operates on a lower-dimensional gridworld. The relative benefit of supervised auxiliary objectives may be smaller in lower-dimensional settings where the encoder has fewer confounds to ignore.

## Confidence reasoning

The paper is competent empirical work published in a peer-reviewed journal, building directly on CURL with a principled modification that specifically demonstrates the value of categorical supervision. It is the closest available published result to SD-009's mechanism. Confidence is set at 0.70 rather than higher because the categorical dimension differs (action vs. event type), the venue is PLOS ONE rather than a top-tier ML conference, and the modality gap to REE's gridworld is real. The paper supports the direction and mechanism of SD-009 clearly enough to count as meaningful positive evidence.
