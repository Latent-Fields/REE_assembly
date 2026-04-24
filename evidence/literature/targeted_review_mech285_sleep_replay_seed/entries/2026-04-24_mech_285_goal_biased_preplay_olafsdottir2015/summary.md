# Olafsdottir et al. 2015 -- goal-biased preplay of unexplored space

## What the paper did

Rats explored a T-maze in which one of the two arms was physically barriered but visually accessible. On some sessions, the experimenters placed visible food in the barriered arm; on others, the barriered arm was identical but unrewarded. Place cells were recorded during exploration and during subsequent rest periods. The analysis asked whether the offline reactivation sequences included the barriered arm -- a region the animal had seen but never physically traversed.

## Key findings relevant to MECH-285

In the rewarded condition, sequences corresponding to the barriered (unvisited) arm appeared in rest-period reactivation at above-chance rates -- "preplay" of a trajectory through space the animal had not sampled. In the unrewarded-but-otherwise-identical control, this preplay did not arise. Critically, the seed states for these sequences could not have been drawn from the current-episode active ensemble in any straightforward sense; they must have been drawn from a pool that included places the animal had only seen.

## Translation to REE

MECH-285's central architectural question is whether the sleep-replay start-state distribution is confined to currently-active anchors (narrow reading) or spans a broader pool that includes anchors the agent has not recently visited (broad reading). Olafsdottir et al. provide proof-of-concept for the broad reading: the seed pool can include places the agent has never been, provided a gating signal marks them as motivationally relevant. Whatever else it does, the biology does not force the narrow-active-only design; the substrate supports broadening.

The caveat: the gating signal here is visible reward, which maps cleanly onto dopaminergic salience-tagging (the MECH-074b / McNamara 2014 arm) rather than onto MECH-285's posited epistemic-staleness arm. Olafsdottir et al. speak to whether broad coverage *can* happen, not to which priority signal drives it. MECH-285's dissociation prediction -- that a calm, low-arousal but high-novelty environment should produce broad coverage weighted by staleness rather than salience -- is orthogonal to this paradigm.

## Limitations and caveats

The unvisited-arm preplay is an effect of seeing reward, not of epistemic uncertainty about that arm. In the MECH-285 framework, this paper sits clearly on the "broad coverage is biologically available" half of the argument, but is weak evidence on the priority-shape half. The study also does not separate awake replay from sleep replay -- rest periods here are brief, and the distinction between waking-quiescence SWR content and full-sleep SWR content (see Karlsson & Frank 2009, Joo & Frank 2018) may matter for whether the observed pattern generalises across states.

## Confidence reasoning

Source quality is high (careful place-cell recording, well-controlled task, top-tier venue). Mapping fidelity is moderate because the paper speaks to one of MECH-285's three architectural questions (seed coverage) but not to the others (priority shape, salience dissociation). Transfer risk is moderate -- rat CA1 to in-silico V_s schema is a substantial inferential leap, and the gating signal here is not the one MECH-285 foregrounds. Aggregate confidence 0.72.
