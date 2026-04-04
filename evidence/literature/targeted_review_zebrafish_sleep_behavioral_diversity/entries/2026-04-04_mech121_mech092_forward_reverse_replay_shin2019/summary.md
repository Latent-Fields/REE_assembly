# Shin, Tang & Jadhav 2019 — Forward and Reverse Replay for Retrospection and Prospection

**Source:** Shin JD, Tang W, Jadhav SP. "Dynamics of Awake Hippocampal-Prefrontal Replay for Spatial Learning and Memory-Guided Decision Making." *Neuron* 104(6):1110-1125, 2019. DOI: [10.1016/j.neuron.2019.09.012](https://doi.org/10.1016/j.neuron.2019.09.012)

**Claims evidenced:** MECH-121, MECH-092

---

## What the paper did

Shin, Tang and Jadhav simultaneously recorded hippocampal CA1 and prefrontal cortex (PFC) ensembles throughout the entire course of spatial alternation learning, from naive to expert performance. During inter-trajectory pauses, they decoded both forward (representing future paths) and reverse (representing past paths) hippocampal replay events and assessed their coordination with prefrontal activity. Crucially, they tracked how the content and direction of replay changed across the learning trajectory.

## Key findings relevant to REE

Reverse hippocampal-prefrontal replay (encoding past paths) dominated early learning and showed a negative learning gradient -- it preferentially represented the paths the animal had just taken, particularly correct vs error choices, supporting retrospective evaluation. Forward replay (encoding anticipated future paths) increased with learning and showed a positive gradient -- it increasingly represented paths the animal was about to take correctly, supporting prospective planning.

Both types were coordinated with prefrontal activity, establishing a hippocampal-to-prefrontal read channel for memory-guided behaviour. The shift from reverse-dominant to forward-dominant replay across learning mirrors the transition from exploratory error-correction to consolidated planning.

Correct and error paths were distinguished in the content of coordinated replay: the system preferentially replayed correct paths more as learning progressed.

## Translation to REE

MECH-121 posits that NREM SWR replay transfers episodic content from E3/hippocampal buffer to E1 neocortical representation. The Shin data provides a functional decomposition of what replay is actually doing: it is not a single homogeneous process but two complementary operations that serve different learning functions. The reverse replay maps onto REE's retrospective harm/benefit attribution -- E3 evaluating past trajectories to update the viability map (what happened, what was the cost). The forward replay maps onto prospective viability map seeding -- E1 building a world model that anticipates future trajectory outcomes.

This has an important implication for MECH-121 and MECH-120's interaction: if replay is to diversify behavioural strategy (the behavioral diversity claim underpinning this literature pull), then the replay content must include not just the dominant trajectory but the road not taken. Reverse replay naturally achieves this when error paths are replayed -- they represent alternatives that were tried and evaluated. A system with only forward replay from the dominant strategy would consolidate that strategy preferentially, reproducing the monostrategy problem from the memory architecture side rather than the SHY side.

For MECH-092 specifically: the quiescent inter-episode replay in V3 is the functional analog of the awake SWR replay studied here. The finding that both forward and reverse content are necessary across learning argues that V3's MECH-092 implementation should eventually support both directions -- not just forward (planning-biased) replay.

## Limitations and caveats

The study focuses on awake inter-trajectory pauses; the relationship to sleep-phase NREM SWR replay (MECH-121) requires an additional inferential step. Whether the forward/reverse distinction maps directly onto the sleep-phase consolidation pipeline (or whether sleep SWRs are qualitatively different in content bias) is not established here. The prefrontal coordination aspect -- hippocampal replay driving PFC readout -- does not have a clear direct REE analog in V3, where the planning module integration is still being developed. The distinction between forward and reverse replay is also harder to define cleanly in non-linear environments; the W-maze affords a clean unidirectional track that may not generalise to the open CausalGridWorld.

## Confidence reasoning

Confidence 0.85 for MECH-121 and MECH-092 combined. High source quality (Neuron, Jadhav lab, longitudinal tracking across full learning trajectory). The functional decomposition into retrospective evaluation and prospective planning is the most direct evidence available that replay serves both halves of the learning cycle that MECH-121 and MECH-092 collectively cover. Docked for the awake-to-sleep generalisation step and the prefrontal integration gap.
