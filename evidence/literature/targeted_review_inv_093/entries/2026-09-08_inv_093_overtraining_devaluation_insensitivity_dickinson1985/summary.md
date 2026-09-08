# Dickinson (1985) -- Actions and habits: the development of behavioural autonomy

**Claim tested:** INV-093 (skill optimisation must not trade harm sensitivity for competence)
**Direction:** supports | **Confidence:** 0.72

## What the paper did

Dickinson sets two models of animal behaviour against each other -- the mechanistic stimulus-response account, in which behaviour is an innate or acquired habit triggered by a stimulus, and the teleological account, in which activities are purposive actions controlled by the current value of their goals -- and argues that both are right, of different behaviours, and that the same behaviour can move from one to the other.

The empirical hinge is outcome devaluation. Train a rat to lever-press for food, then devalue the food (pair it with illness, or sate the animal on it specifically), then test in extinction. If the response is goal-directed, it drops: the animal is pressing *for* something whose value has changed. If it is habitual, it persists: the lever-press has become autonomous of what it produces. Dickinson's result is that a simple food-rewarded activity is sensitive to devaluation after *limited* training but not after *extended* training. Behavioural autonomy is a product of practice.

## Why this matters for INV-093

The two ML entries in this directory both show harm-sensitivity degradation arising from something that has gone wrong -- a misspecified proxy in Pan et al., a gradient update overwriting a shallow alignment layer in Qi et al. Both invite the reply that INV-093 is really a caution about sloppy objectives, dischargeable by better engineering. This paper is the answer to that reply, and it is the reason I have weighted a 1985 rat study alongside two recent ML results.

Here nothing has gone wrong. The outcome value is correct and known. There is no adversary, no proxy, no specification error. The animal is *more* competent than it was, not less. And refinement alone -- the sheer amount of practice that made the behaviour good -- has severed the link between the behaviour and the value of what it produces. Behavioural autonomy is not a failure of the learning system; it is the learning system working, buying speed and reliability by dropping the outcome-value query from the loop.

For REE this changes what INV-093 is. If the project's brain-like-construction commitment means anything, then a skill-refinement mechanism built along these lines will do this by default, and harm-sensitivity degradation under refinement is the *expected* behaviour of a well-functioning system rather than a bug to be designed out. INV-093's floor stops being precautionary and becomes structural: something has to actively hold the outcome-value channel open against a refinement process whose whole efficiency gain comes from closing it. That is a substantially stronger reading of the claim than "watch out for trade-offs", and it is what this paper licenses.

It also supplies the probe design. The overtrained and the moderately trained animal are behaviourally identical until the devaluation. There is no signal in ordinary performance. Whatever REE builds to test INV-093 has to *actually perform a revaluation* -- make something newly harmful mid-sweep and see whether behaviour tracks it -- because reading the intact-condition behaviour, however carefully instrumented, will show nothing.

## Limitations and caveats

The decisive gap, and I do not want it buried: outcome devaluation is not harm. This paper shows insensitivity to a change in outcome *value*. INV-093 is about sensitivity to harm, to other-agent signals, and to commitment violation. Treating a newly aversive outcome as a special case of a revalued outcome is an argument REE has to make explicitly and, as far as I can see, has not yet made anywhere. The Jones et al. (2024) entry in this directory exists precisely because it takes one empirical step across that gap -- punishment, not devaluation -- and it should be read as the completion of this one.

Two further caveats. This is rat instrumental conditioning; there is no computational mechanism here that REE could port, only a phenomenon to be reproduced or not. And the human habit-induction literature since has a poor record -- de Wit et al. (2018) report five failures to induce habits experimentally in humans by the training-duration route -- so whether "extended training produces autonomy" generalises across species is genuinely contested rather than settled. I read that as a caution about the *strength* of the effect in complex agents, not about its existence, but it is a real discount.

## Confidence reasoning

Source quality 0.85: the founding statement of the action/habit distinction, over a thousand citations, with the core rodent devaluation effect replicated for four decades; held below 0.90 by the contested human record. Mapping fidelity 0.70 -- the *structure* (training duration causes autonomy from outcome value) maps exactly onto INV-093, while outcome value standing in for harm sensitivity does not, and that substitution is this entry's main weakness. Transfer risk 0.45: rat conditioning to an artificial agent's ethical panel is a long transfer, mitigated rather than removed by REE's explicit commitment to brain-like construction, which makes this literature a statement of design expectation rather than a loose analogy. Aggregate 0.72.
