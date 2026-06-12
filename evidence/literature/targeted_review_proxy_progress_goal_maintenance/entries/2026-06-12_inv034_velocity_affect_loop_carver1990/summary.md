# Carver & Scheier (1990) -- the velocity loop as a progress-feedback maintenance signal

**Claim strand:** A -- rate-of-progress feedback sustains goal commitment over long horizons.
**Wires to:** INV-034 (goal maintenance necessary for ethical agency), INV-053 (maintenance failure = depression), and the prospective candidate `progress_velocity_maintenance`.

## What the paper does

Carver & Scheier take their cybernetic (feedback-control) model of behaviour -- in which a first-order loop acts to reduce the discrepancy between a current state and a goal reference value -- and add a *second-order* loop. The crucial move: the second loop does not monitor the discrepancy itself but the **rate** at which the first loop is closing it (its velocity), and compares that rate to a *reference rate*. The output of this second loop is **affect**. Progress faster than the reference rate yields positive affect; slower yields negative affect. Affect, on this account, is a readout of how well the behavioural control system is doing its job over time -- not a readout of how far the goal still is.

## Findings that matter for REE

From the official abstract: "a second feedback system is postulated that senses and regulates the rate at which the action-guiding system is functioning. This second system is seen as responsible for affect." And the error-signal mapping: "Negative affect is proposed to occur when progress is slower than expected or needed and positive affect when progress is faster than expected, needed, or desired."

This is exactly the signal Daniel's thought reached for -- the "window of effort and progress and feedback" in which a superordinate goal can be held alive. The theory says the system already carries a derivative-of-progress signal, and that signal is affectively tagged. That gives REE a principled source for a *maintenance* signal that is distinct from the proxy-goal-for-reachability machinery already owned (INV-065, MECH-216/217, ARC-051): those let a bounded-horizon planner *reach* a distal target; the velocity loop is about whether the goal stays *committed* while the terminal payoff is silent.

## The caveat that must not be glossed

The theory carries a counter-intuitive behavioural prediction: "Negative affect then leads to investing more effort (pushing) and positive affect leads to investing less effort (coasting)." Above-reference progress *reduces* effort on the current goal and licenses redeployment elsewhere. A REE implementation that naively treats positive progress-affect as reinforcement that *increases* commitment to the same goal would invert the theory. This is the single most important transfer risk, and it interacts directly with the disengagement literature already in the repo (`targeted_review_goal_disengagement`).

## Confidence

0.70. The source is foundational and the mapping to a progress-derivative maintenance signal is clean, but the 1990 article is theoretical synthesis rather than a controlled test, and the loop is specified only qualitatively -- reference-rate setting, the velocity->affect gain, whether affect tracks instantaneous or predicted rate, and multi-goal arbitration are all left to the modeller. Honest direction: supports the *existence* and *shape* of the mechanism; does not adjudicate the maintenance-vs-reachability distinction, which is REE's to draw.
