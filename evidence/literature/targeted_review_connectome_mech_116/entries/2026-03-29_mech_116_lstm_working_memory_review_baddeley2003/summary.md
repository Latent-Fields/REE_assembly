# Baddeley (2003): Working memory -- looking back and looking forward

**Claim tested:** MECH-116 -- E1's LSTM hidden state serves as working memory substrate for goal representation

## What the paper did

Baddeley's 2003 Nature Reviews Neuroscience paper revisited the working memory framework he and Hitch introduced in 1974 and updated it to include the episodic buffer -- a component he added explicitly in 2000 to handle the problem of integrating information from multiple sources. The original three-component model (central executive, phonological loop, visuospatial sketch pad) was powerful but left unexplained how a person can hold a coherent scene or narrative in mind when neither the phonological loop nor the visuospatial sketch pad alone could account for it. The episodic buffer is a temporary, multimodal, capacity-limited store that binds information from different sources -- including long-term memory -- into unified episodes. The 2003 paper synthesizes evidence for this revised architecture and places the neural correlates discussion in the context of frontal lobe involvement and hippocampal contributions.

## Key findings relevant to MECH-116

The most important structural point for MECH-116 is Baddeley's characterization of the central executive as the attentional controller that maintains goal-relevant representations and directs processing resources. The central executive is the component that holds "what I am currently trying to do" -- the goal context -- and distributes this context to the subsidiary systems. This is functionally close to what MECH-116 claims for E1: maintaining goal context and making it available (via theta-rate output) to the downstream planning system (E3). The episodic buffer is also relevant: it is the component that integrates long-term memory with current working memory content, which maps to E1's role in integrating z_goal_latent (a structured latent derived from prior learning) with current z_world and z_self inputs.

## REE translation

In REE terms, the central executive maps to E1 (goal context maintenance, recurrent integration), the phonological loop and visuospatial sketch pad map to the various sensory encoding streams (z_world, z_self channels), and the episodic buffer maps to the theta-packaged integration that occurs when E1 passes its output through ARC-032's ThetaBuffer to E3. Baddeley's claim that the episodic buffer "provides a temporary interface between subsystems and with long-term memory" maps to E1's role as the component that holds z_goal_latent in a form accessible to E3's trajectory scoring. The functional architecture is strikingly parallel.

## Limitations and caveats

The Baddeley framework is a cognitive-psychological model, defined by behavioral dissociation experiments and psychophysical capacity measures. It does not directly specify neural implementation, and the mapping from Baddeley's components to prefrontal circuits requires additional steps (Goldman-Rakic, D'Esposito, Petrides and others provide the neural grounding). More specifically for MECH-116, the "central executive" in Baddeley's framework is something of a theoretical residue -- the component that does everything the other components do not -- rather than a precisely characterized mechanism. This means that mapping E1's LSTM recurrence to the central executive requires care: it is a conceptual alignment, not a mechanistic derivation. The Baddeley 2003 paper supports the claim that working memory is an active, multi-component maintenance system with a goal-context-holding executive, but does not speak directly to whether LSTM recurrence is the right computational substrate.

## Confidence reasoning

Confidence is 0.65. The paper provides strong conceptual support -- the architecture Baddeley describes is recognizably parallel to REE's E1/E3 division -- but the mapping fidelity is limited by the cognitive rather than neural level of description, and the transfer risk is elevated because the LSTM claim is specific to a neural-computational mechanism that Baddeley's framework does not address. Best treated as a theoretical frame that motivates the MECH-116 analogy, not as direct mechanistic evidence.
