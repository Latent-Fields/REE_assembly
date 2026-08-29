# Tseng et al. (2022) — a dedicated threat channel gates sleep, and it is not a damage readout

**Claim tested:** MECH-492 (MECH-286's sleep-permission threat conjunct is an uncalibrated, undeclared-source consumer of the shared `z_harm_a.norm()` expression)
**Direction:** supports (architectural premise only — see the caveat)

## What the paper did

Tseng and colleagues asked a narrow question with a wide consequence: when a sleeping animal is threatened, what wakes it, and is that machinery the same machinery that puts it to sleep in the first place? They recorded from and manipulated a population of CRH-expressing neurons in the medial subthalamic nucleus of mice, with EEG/EMG sleep staging, while presenting predator stimuli across several sensory modalities — visual, auditory, olfactory. The manipulations are causal, not correlational: cell-type-specific optogenetic and chemogenetic gain- and loss-of-function, with the projection to lateral globus pallidus identified as the effector arm.

Three findings matter here. First, predator stimuli produce immediate arousal from REM sleep, more readily than from NREM. Second, the mSTN CRH population mediates that arousal and the accompanying defensive response, and does so for threats arriving through *multiple* sensory channels — it is not a modality-specific reflex arc. Third, the same neurons participate in ordinary REM regulation and in the adaptive REM increase that follows sustained predator stress. One population, wearing both the safety hat and the sleep-regulation hat.

## What this says about MECH-492

MECH-492 is a substrate-defect claim, so the honest framing matters: this paper is not evidence *about REE's code*. What it supplies is the biological form of the architectural expectation MECH-492 says the implementation quietly fails to meet.

The claim's core is that `threat_ok = z_harm_a.norm() < 0.4` reads an expression whose informativeness about place safety is inherited from whichever sourcing mode an unrelated driver happens to set, and that MECH-286 declares no sourcing mode of its own. Tseng et al. show what the corresponding biological signal actually is: a dedicated, anatomically identified population, driven by *exteroceptive* predator cues, with its own downstream pathway. It is emphatically not a repurposed interoceptive readout of tissue damage. An animal that only refused sleep once something had already bitten it would not be an animal for long — and that is close to the regime a damage-sourced threat term puts the REE agent in.

So the paper strengthens two things. It strengthens MECH-492's premise that *sourcing is architecturally load-bearing* for a sleep-onset threat term, rather than an implementation detail one can leave to the driver. And it independently strengthens the routing decision recorded under SD-MECH303-THRESHOLD-SOURCING — build a dedicated proximity-anticipatory safety signal rather than re-point the shared `z_harm_a` expression and break its other nine consumers. Biology, here, took option (a) too.

There is a second, less obvious point in the finding that the same cells do both jobs. MECH-492 predicts that a near-constant conjunct silently degrades a three-way AND into an effective always-permit. Tseng et al. suggest the damage would not stop at the safety function: if REE ever consolidates threat-sensing and sleep-regulation onto one signal the way the mSTN does, a miswired source corrupts both roles at once.

## Limitations, stated plainly

This is an argument from design, and it should not be dressed up as more. The paper says nothing about REE, nothing about `z_harm_a`, and nothing about threshold calibration. MECH-492's two sharpest legs — that the 0.4 default was chosen before any measurement of the signal existed, and that the conjunction degrades to always-permit — receive **no** support here whatsoever. Those rest on V3-EXQ-917's threshold sweep and V3-EXQ-950's measured AUC of 0.5016 / 0.4966, which is where the claim's real weight sits.

Two further caveats. The mapping from "predator cue arriving across modalities" to REE's "place safety" is looser than it looks; predator presence and location hazard are correlated constructs, not the same construct, and the paper's stimuli are object-like rather than place-like. And the fact that biology built a dedicated channel does not logically entail that a shared channel *must* fail — plenty of shared signals work. The empirical demonstration that this particular shared signal measures at chance is experimental evidence, not literature evidence.

## Why confidence 0.74

Source quality is high (0.90): Neuron, causal circuit dissection, defined projection target, multimodal stimuli. Mapping fidelity is only moderate (0.62) because the paper grounds the architectural premise and not the defect. Transfer risk is moderate-to-high (0.40): rodent circuit to artificial agent gate is a long transfer, and for a substrate-defect claim literature is properly context rather than adjudication. The aggregate sits above the components' mean on source quality but is deliberately held under 0.8 — this entry earns its place by telling us what the term *should* have been wired to, not by telling us what it is.
