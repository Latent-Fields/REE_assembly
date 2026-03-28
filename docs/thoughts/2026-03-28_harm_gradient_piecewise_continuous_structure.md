# Thought: Harm Gradient Has Piecewise-Continuous Structure

**Date:** 2026-03-28
**Source:** Observation from literature pull ARC-024 session (Fanselow 2022 / predatory imminence continuum)
**Status:** unprocessed

## Observation

During the ARC-024 literature pull, a nuance emerged from the Fanselow predatory imminence continuum (PIC) that is not captured by ARC-024. ARC-024 claims harm signals have a *continuous gradient* structure. PIC theory shows the biological reality is *piecewise-continuous*: behavioural response *form* (topography) transitions **discretely** at threshold imminence levels (pre-encounter → post-encounter → circa-strike), while response *vigour* varies continuously within each mode.

This is not a contradiction of ARC-024 — ARC-024's architectural claim (gradient world is necessary and learnable) holds. But it is a separable, testable prediction about the *shape* of the learned harm representation.

## Candidate claim

> "The world harm-gradient encodes both a continuous intensity dimension and discrete mode-transition thresholds. E3.harm_eval should learn not just a graded intensity signal but a piecewise representation with phase transitions at critical proximity levels."

This could register as:
- **MECH-xxx** (mechanistic): `harm_eval.piecewise_gradient_structure` — E3's harm representation has discrete mode transitions driven by threshold crossings in the continuous gradient, corresponding to the pre-encounter/post-encounter/circa-strike modes.

## Testing implications

- V3 test: Does E3.harm_eval's output distribution show bimodal or trimodal structure rather than unimodal gradient? Does the distribution of harm_eval scores cluster around 2-3 modes (e.g. none/low, approach/medium, contact/high) with gaps between them, rather than a smooth continuous distribution?
- V4 test: Can an agent learn to transition between qualitatively different defensive strategies (routing modification, freezing, emergency escape) at distinct harm-gradient thresholds?

## Notes

- Mobbs 2007 provides human neural evidence: the vmPFC → PAG shift is itself a discrete transition (not a purely smooth gradient) at threshold threat imminence.
- The mode-switching structure may be important for safety: a pure gradient representation would not trigger emergency responses until harm is already very high; threshold-based mode transitions allow abrupt escalation.
- Likely V4-scope to test the full three-mode structure; V3 could test the binary presence/absence of mode transitions in harm_eval output distribution.
- Depends on: ARC-024 (gradient exists), MECH-071 (drive architecture for goal-directed behaviour — panic mode may require its own drive).
