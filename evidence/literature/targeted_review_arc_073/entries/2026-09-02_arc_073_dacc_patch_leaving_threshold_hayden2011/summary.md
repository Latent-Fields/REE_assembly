# Hayden, Pearson & Platt (2011) -- Neuronal basis of sequential foraging decisions in a patchy environment

*Entry for ARC-073: play-to-real transition is triggered by competence saturation or drive pressure, not by scheduled duration.*

## What the paper did

Macaques performed a virtual patch-foraging task: each patch delivered rewards that depleted with successive harvests, and the animal chose on every trial whether to stay or to pay a travel cost and move to a fresh patch. Travel time was manipulated across blocks. The authors recorded single units in dorsal anterior cingulate cortex while the animals made these sequential stay-or-leave decisions.

The result is unusually clean for a decision-variable claim. dACC neurons fired during each stay decision, and their firing rose across successive decisions within a patch until it reached a threshold, at which point the animal left. For a given travel time, that leaving threshold was fixed. Increasing travel time did two things at once: it reduced the gain of the stay-response and raised the leaving threshold. These joint modulations tracked behaviour better than any single task variable did.

## Why this matters for ARC-073

ARC-073 makes a claim about the *form* of a disengagement rule. It says the agent should leave play when the thing play is producing -- world-model learning, indexed by |d(PE)/dt| -- stops arriving, and it explicitly denies that a clock does the work. The question I want to ask of the literature is not "does the brain compute learning progress?" but the prior one: is a monitored-quantity-plus-threshold the kind of thing a brain actually uses to end an engagement, or is that an engineer's idealisation?

This paper answers that prior question affirmatively, and with a canonical result. A well-studied primate disengagement decision is implemented as an accumulating value signal crossing a threshold. It is not implemented as elapsed time. So the shape ARC-073 proposes -- monitor a scalar, threshold its decline, close the episode -- has a real precedent, and REE is not inventing a mechanism with no biological analogue.

The travel-time manipulation is the part I find most useful, and it speaks to the second trigger in the claim's notes rather than the first. The leaving threshold was not a property of the patch alone; it moved with the cost of the alternative. That is the same structure as the claim's competition criterion ("real homeostatic drive_level exceeds synthetic z_goal benefit_exposure") -- the exit condition is set jointly by what you are leaving and by what is waiting. It also suggests that a single scalar `play_lp_saturation_threshold` in GoalConfig, fixed across contexts, is under-specified relative to what the biology does. A threshold that ignores the value of the real task an agent would return to will fire at the wrong time when that value changes.

## Where the mapping strains

The depleting quantity is exogenous. The patch empties whether or not the monkey learns anything; depletion is a fact about the environment. ARC-073's quantity is endogenous -- PE falls *because* the agent got better. Formally similar, causally opposite. A criterion tuned on an exogenous depletion signal will fire happily on an environment that is merely unrewarding, which in REE terms means closing a play episode because the world stopped being informative rather than because the agent mastered it. Distinguishing "I have learned this" from "there was never anything here" is precisely the discrimination this study never has to make, and it is one REE will have to.

There is also a level mismatch. Patch-leaving is a within-mode choice: this patch versus the next patch, same behavioural mode throughout. ARC-073 is a between-mode transition: synthetic z_goal play versus homeostatically driven real behaviour, with MECH-196 closing the episode. Assuming those are the same computation because they share a threshold-crossing signature is the main over-reach available here, and I have kept `mapping_fidelity` at 0.62 to mark it.

## Confidence

0.66. Source quality is high -- Nature Neuroscience, macaque single units, a result that has held up and been extended in rodents (see the Kane et al. 2022 entry in this directory, which complicates it). The discount is entirely in the mapping. This is strong evidence for the *form* of ARC-073's criterion and no evidence at all for its *content*. Recorded as `supports` because ARC-073 is an architecture_hypothesis and the form is what such a claim is mostly asserting; a reader who wants evidence that learning progress specifically is monitored and thresholded should look to the Colas et al. 2019 entry, and will find that half thinner than they hoped.
