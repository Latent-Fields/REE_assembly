# From Spontaneous Ignitions to Sensorimotor Cell Assemblies via Dopamine: A Spiking Neurocomputational Model
**Griffin, Mattera, Baldassarre & Garagnani (2026) -- Brain Sciences**

## What the paper did

Griffin and colleagues built a neurobiologically constrained spiking neural network model consisting of six brain areas (three pre-central motor-related and three post-central sensory-related), with biologically constrained within- and between-area connectivity. They simulated two developmental phases: (1) an initial Hebbian exploratory phase where the network self-organizes action-perception circuits through spontaneous motor babbling (noise-driven spontaneous ignitions), and (2) an exploitation phase where a global dopamine reward signal reinforces a subset of circuits that enable access to biologically salient stimuli. Hand action execution and haptic perception are simulated as activity in primary motor and somatosensory model areas.

## Key findings

During the Hebbian exploratory phase, the network autonomously developed action-perception cell assemblies corresponding to multiple possible hand actions (flexion, extension, touching, pushing) without any external reward. The key mechanism is spontaneous (noise-driven) ignition of partially formed circuits, with Hebbian learning strengthening co-active connections. During the exploitation phase, positively reinforced circuits increased in size and frequency of spontaneous ignition relative to non-rewarded ones. The transition from exploration to reward-seeking was spontaneous -- it emerged from the network's own dynamics as cell assemblies matured.

## REE translation

This paper provides the most direct computational evidence for REE's infant-stage design problem. The two-phase architecture is the key insight: Phase 1 (Hebbian self-organization via babbling) must precede Phase 2 (reward consolidation) for the agent to have any option diversity for the reward mechanism to select from. An agent that starts with reward learning from the first step, with no prior exploration phase, has no variety of action-outcome associations to distinguish -- it converges on whatever actions happen to produce early rewards, producing monostrategy.

The parallel to REE is direct: E3's CEM diversity mechanisms (MECH-313/314/320) are the functional analog of Phase 1's Hebbian self-organization. The current substrate goes straight to reward-weighted CEM selection; the Griffin model says this needs a Phase 1 period where the CEM generates diverse candidates without reward weighting to build the option library first.

## Limitations and caveats

Simulation only; no direct comparison with infant neurophysiological data on cell assembly formation rates. The dopamine global reward signal is a simplification; in real development, neuromodulatory gating is context-specific. The model is tested only on hand actions; generalization to locomotor or whole-body movement repertoires is unverified.

## Confidence reasoning

Brain Sciences is a broad-scope journal and this is a simulation paper, so source quality is moderate. However, the computational architecture is neurobiologically constrained and the two-phase result has strong conceptual grounding. Confidence 0.76, reflecting high conceptual relevance but moderate empirical weight.
