# Most, Scholl, Clifford & Simons (2005) -- What you see is what you set

**Claim tested:** INV-092 | **Direction:** supports | **Confidence:** 0.68

## What the paper did

A *Psychological Review* target article unifying two literatures that had grown up separately: inattentional blindness (failures to notice unexpected objects while attention is engaged elsewhere, measured as *awareness*) and attention capture (automatic attentional shifts, measured *implicitly* through reaction times and errors). The authors argue many but not all aspects of capture apply to inattentional blindness, and that the two classes of phenomena remain importantly distinct. Their central empirical conclusion is that the most influential factor determining whether an unexpected object is noticed is the observer's own attentional goals -- the current attentional set -- rather than properties intrinsic to the object.

## Why this matters for INV-092

INV-092 requires a suppressor to distinguish four things that all present as "input competing with the current goal": irrelevant distraction, legitimate interruption, urgent harm, and newly-relevant other-agent state. The question this paper answers is whether that discrimination might emerge for free from a competently built suppressor. It says no, and it says why.

The organising variable in human suppression is *set match* -- does this input resemble what I am currently looking for? Importance is orthogonal to set match. An urgent cue that happens not to share the goal's features occupies exactly the same position as an irrelevant distractor, and is treated identically. That is the failure INV-092 forbids, arriving not through bad design but through the ordinary operation of a set-keyed suppressor. Which means the four-way discrimination has to be built as an explicit, separately-implemented gate. It is not a property that a well-tuned salience or goal-relevance mechanism acquires as a side effect of being well-tuned.

The awareness-versus-performance distinction the paper draws is the second contribution, and it is a measurement warning rather than a design one. Inattentional blindness is invisible to performance measures: the signal was never registered, so there is no slowed response, no error, and nothing anywhere in the goal-task record indicating that anything was missed. A falsifier panel that instruments only downstream task behaviour cannot see this class of miss at all. It has to score whether the injected signal was *registered*, separately from whether task performance degraded. This is the same structural point MECH-467 makes in distinguishing rule corruption from behavioural capture -- an intact rule producing a clean-looking trace while the safety-relevant event went unreported -- which is why MECH-467 is tagged here even though this entry does not test it directly.

There is a practical consequence for how the sweep is built. If suppression is set-keyed, raising it will raise the miss rate for *off-set* inputs specifically. An injected harm cue that shares features with the goal-relevant stream is therefore the wrong probe; it will ride through on set match and the sweep will measure nothing. The injected signal has to be deliberately off-set, which is also the honest version of "weak evidence" in INV-092's own wording.

## Limitations and caveats

The unexpected objects in this literature are affectively neutral moving shapes. Nothing here demonstrates that a genuinely threatening or socially urgent stimulus obeys the same set-match rule, and there is a competing literature -- see the Pessoa (2002) entry in this directory, and the dispute noted there -- arguing for at least partially privileged access for affective stimuli. What transfers is a *default*: suppression is set-keyed and importance-blind unless something is built to make it otherwise. That is not the same as a demonstration that harm cues are missed, and this entry should not be read as one. The paradigm is also sustained visual monitoring in humans, a narrower control surface than REE's suppression of competing input to a committed goal.

## Confidence reasoning

Source quality 0.85 -- a *Psychological Review* target article by the field's principal investigators. Mapping fidelity 0.60: the step from "set match governs noticing" to "harm cues will be missed" is an inference REE is making, not a result reported. Transfer risk 0.50: the set-match principle is general enough to survive the move to an artificial suppressor; the noticing rates certainly are not. Aggregate 0.68, which reflects that this entry is doing structural rather than empirical work -- it establishes that INV-092's constraint is *needed*, and says nothing about whether any particular REE mechanism violates it.
