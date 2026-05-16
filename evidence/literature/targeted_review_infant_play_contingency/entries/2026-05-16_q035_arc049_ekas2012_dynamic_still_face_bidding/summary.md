# Summary: Ekas, Haltigan, Messinger (2012) -- Dynamic Still-Face Effect

**Source:** Ekas, N.V., Haltigan, J.D., Messinger, D.S. (2012). The dynamic still-face effect: do infants decrease bidding over time when parents are not responsive? Developmental Psychology, 49(6), 1027-1035. doi:10.1037/a0029330

**Claim IDs:** Q-035, ARC-049, INV-059

**Evidence direction:** supports | **Confidence:** 0.78

## Key Finding

Within the still-face episode, infant social bidding (smiling while gazing at parent), gaze, and smiling all decrease progressively over time, while cry-face increases. Hierarchical linear modelling captures this within-episode dynamic trajectory, not just between-episode differences. The trajectory predicts attachment security and infant internalizing problems -- establishing individual-difference validity.

## REE Relevance

First rigorous quantification of the within-episode temporal dynamics of frame monitoring during a contingency failure. The progressive decline in bidding shows that the monitoring system generates a time-series of frame-state updates, not a one-shot violation detection.

For Q-035: the monitoring architecture generates a continuously-updating frame confidence signal. Frame confidence decays toward zero across successive monitoring cycles that return 'partner still unresponsive'. This implies the REE frame state is not binary but has a decay function over time-since-last-contingency.

For ARC-049: the bilateral play frame tag requires a frame confidence scalar (or distribution) with temporal decay properties, not a binary open/closed state. The progressive bidding decrease maps onto this: each successive check returns violation, so frame confidence decrements.

For INV-059: the bidding behavior itself is a repair attempt -- the infant is trying to re-establish mutual frame maintenance. The escalation of cry-face as bids fail to work shows what happens when INV-059's necessity condition is violated without repair.

## Limitations

- HLM captures population-level trajectories; cannot determine within-infant sampling rate.
- Progressive bidding decrease could reflect fatigue or regulatory state rather than explicit monitoring.
- Still-face conflates monitoring with social stress.

## Action

Supports Q-035, ARC-049, INV-059. Suggests implementation metric: REE frame confidence should decay monotonically when contingency signal fails, then restore on reunion. The bidding-as-repair-attempt behavior could be operationalised as an action the REE agent takes when frame confidence drops below threshold.
