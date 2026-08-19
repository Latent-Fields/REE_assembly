# Context inference as an active, persistent control process

**Status:** Provisional thought intake  
**Date:** 2026-08-19

## Core thought

ContextMemory should probably not be treated as a passive nearest-match lookup. In an organism operating in ambiguous environments, the important question is not simply “which stored context looks most similar?” but “which latent situation best explains what is happening, and is the evidence strong enough to justify changing the currently active interpretation?”

A useful context mechanism may therefore require several coupled functions:

- assessment of how well the current context explains incoming experience;
- uncertainty over competing contexts;
- detection of an epistemic deficit when available evidence is insufficient;
- active orienting or information-seeking to obtain discriminating evidence;
- comparison of candidate contexts;
- hysteresis or persistence so that small fluctuations do not continuously switch the organism between interpretations;
- an exploitation or action window after a context has been selected, during which the organism can act on that interpretation rather than immediately reopening inference;
- a criterion for when none of the stored contexts adequately explains experience and a new contextual representation should be formed.

The persistence requirement matters in both directions. Context should not be abandoned too easily, but once a context is selected the organism may also need enough uninterrupted time to exploit it. Otherwise a highly uncertainty-sensitive agent risks becoming permanently epistemic: continuously checking, rarely acting.

## Architectural implication

Context inference may be a loop spanning ContextMemory, uncertainty, orienting, hippocampal processing, cue acquisition, and commitment rather than a function local to the memory module:

**active context → prediction/behaviour → mismatch → uncertainty → orienting/information acquisition → candidate-context comparison → retain/switch/create → temporary commitment to action**

This need not imply a new executive module. Existing REE signals and mechanisms may implement different parts of the loop.

## Important distinction

Large prediction error alone should probably not mean “new context.” A startling event, noise, gradual environmental drift, and a genuine latent-state transition can all produce prediction error but should not necessarily trigger the same response.

The more relevant quantity may be **persistent, structured evidence that the currently inferred latent situation no longer explains observations or their action consequences**.

## Experimental form

Construct environments that are perceptually similar but require opposing policies. For example, two contexts could contain almost the same cues while the correct action toward one object differs according to the hidden causal situation.

Test whether REE:

- maintains the active context despite minor ambiguity;
- orients when evidence becomes insufficient;
- seeks cues that discriminate between alternatives;
- switches when evidence genuinely favours another context;
- remains in the selected context long enough to exploit it successfully.

Control conditions should include transient surprise, gradual drift, and abrupt context change.

## Potential falsification

If context switching can be explained entirely by simple similarity retrieval or unsigned prediction error, the larger mechanism is unnecessary. Conversely, if adding uncertainty, orienting, and hysteresis does not improve hidden-context discrimination or produces pathological indecision, this formulation is wrong or overbuilt.

## Open questions

- What determines context inertia?
- What signal terminates orienting?
- When should mismatch update the existing context, retrieve another, or create a new one?
- Should the active context include internal variables such as current goal, bodily state, confidence, or inferred social situation rather than primarily sensory scene identity?

## Intake note

This is a thought intake, not an architecture claim. It should be checked against existing REE claims and mechanisms before promotion, especially ContextMemory, orienting/epistemic-deficit machinery, hippocampal processing, uncertainty, and commitment.
