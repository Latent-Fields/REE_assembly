# Literature Summary: 2026-03-16_mech091_phase_reset_information_transmission_pmc2015

## Claims Tested

- `MECH-091`

## Source

- Engel AK, Gerloff C, Hilgetag CC, Nolte G (2013). *Phase-resetting as a tool of information transmission*. Current Opinion in Neurobiology.
- DOI: `10.1016/j.conb.2012.12.008`
- URL: `https://pmc.ncbi.nlm.nih.gov/articles/PMC4375052/`

## Source Wording

Salient or unexpected stimuli trigger phase-alignment of ongoing neural oscillations rather than simply adding a new signal amplitude component. Thalamocortical neurons act as phase detectors, forcing oscillator alignment when a salient event occurs. This is the mechanistic basis of event-related potentials including P300 (which is strongly associated with event-related theta-band phase reset). Phase-reset ensures that the post-event processing window begins at a coherent reference phase, preventing partial-integration artefacts from mid-cycle updates.

## REE Translation

MECH-091 (salient events phase-reset E3 heartbeat): High-salience events (action sequence completion, unexpected harm, commitment boundary crossing) reset the phase of E3's heartbeat oscillator. The MD thalamus (ARC-023 substrate for E3) acts as the phase-reset mediator. Phase reset guarantees that harm estimates from the triggering event enter E3's stream at the start of a fresh heartbeat cycle. In multi-action plans (W0→W1→W2), each waypoint completion phase-resets E3's clock, so each sub-completion produces a coherent starting condition for the next planning cycle.

## Caveat

The reviewed literature focuses on sensory/oddball paradigms (alpha and theta oscillations) rather than BG-thalamo-cortical completion-event contexts. The specific mapping of completion-of-action-sequence to a phase-reset trigger is a REE architectural extension of the general phase-reset mechanism — plausible but not directly evidenced. The thalamic substrate (MD for E3 heartbeat reset) is inferred from ARC-023 rather than demonstrated in this source.

## Direction and Confidence

- `evidence_direction`: `supports`
- `confidence`: `0.68`
