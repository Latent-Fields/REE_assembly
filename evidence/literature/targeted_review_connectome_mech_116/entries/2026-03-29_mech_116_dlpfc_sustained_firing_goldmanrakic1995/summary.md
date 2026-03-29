# Goldman-Rakic (1995): Cellular basis of working memory

**Claim tested:** MECH-116 -- E1's LSTM hidden state serves as working memory substrate for goal representation

## What the paper did

Goldman-Rakic presented the culminating synthesis of a decade of single-unit recording work in awake behaving primates performing spatial delayed-response tasks. The paradigm is simple but revealing: the animal is shown a spatial cue (a light briefly appearing in one of several locations), then waits through a delay period of 2-5 seconds with no cue present, then must respond to the remembered location. During this delay, approximately 30% of sampled DLPFC neurons sustain elevated firing rates that are selective for the cued location -- they fire more for "cue was to the left" than "cue was to the right," and maintain this selectivity in the absence of any sensory input. Goldman-Rakic argued that these cells are the cellular substrate of working memory: not a passive buffer but an active process of information maintenance through recurrent excitatory circuits within DLPFC.

## Key findings relevant to MECH-116

The core finding is that DLPFC neurons maintain task-relevant information recurrently, without ongoing sensory drive. This is a content-selective, time-extended, intrinsically maintained representation -- precisely the functional properties MECH-116 attributes to E1's LSTM hidden state when conditioned on z_goal_latent. Goldman-Rakic also showed that DLPFC lesions selectively impair delay-period performance while leaving perception and motor execution intact, isolating the working memory function. A further implication -- made more explicit in later work -- is that this maintenance is not merely storage but active routing: the sustained DLPFC representation gates downstream systems toward goal-relevant processing.

## REE translation

MECH-116 proposes that E1's LSTM hidden state h_t is the computational analog of this sustained firing. When E1 is conditioned on z_goal_latent, the goal context enters E1's recurrent dynamics and is maintained across steps without needing continuous re-injection. The biological parallel holds at the functional level: both the DLPFC neuron and the LSTM cell maintain content across time via recurrent dynamics rather than external refresh. The LSTM's gating mechanism (forget gate, input gate) is a learned approximation to the active maintenance that NMDA receptor dynamics and recurrent excitation achieve in cortex.

## Limitations and caveats

Two caveats matter. First, mechanistic: biological persistent activity depends on specific synaptic (NMDA-mediated plateau potentials) and circuit (recurrent excitatory collaterals) mechanisms with no direct LSTM counterpart. The analogy is functional, not mechanistic. Second, content: Goldman-Rakic's cells maintain the location of a sensory cue that has already occurred -- retrospective spatial working memory. MECH-116 claims E1 maintains goal context -- prospective motivational content. These overlap but are not identical. Goal context in REE is more like the "what I am working toward" class of prefrontal representations (closer to rule-maintenance work in DLPFC, e.g., Miller & Cohen 2001) than the pure cue-location delay-period firing Goldman-Rakic studied. This does not undermine the analogy but narrows it.

## Confidence reasoning

Confidence is set at 0.82. Source quality is very high -- this is a landmark, heavily cited paper from a foundational experimentalist. Mapping fidelity is moderate: the functional parallel is clear, but the mechanistic and content differences prevent a full mapping score. Transfer risk reflects the biological-to-computational gap inherent in any claim of this type. Overall, this paper provides strong structural support for MECH-116 as a biologically grounded claim, while leaving open the question of whether E1's LSTM recurrent dynamics are actually sufficient to sustain goal context -- which depends on training and architecture details not tested by Goldman-Rakic.
