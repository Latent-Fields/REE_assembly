# Summary: Murray and Trevarthen (1985) -- Double Video Contingency

**Source:** Murray, Lynne and Trevarthen, Colwyn (1985). Emotional regulation of interactions between two-month-olds and their mothers. In Social Perception in Infants (Field and Fox, eds).

**Claim IDs:** Q-035, ARC-049

**Evidence direction:** supports | **Confidence:** 0.82

## Key Finding

Two-month-old infants watching live (contingent) vs. time-delayed replay (non-contingent) video of their mother show significantly reduced positive affect and gaze during replay, despite identical visual and auditory content. The only manipulation is temporal: the replay is the same facial expressions and vocalizations but shifted in time so they no longer respond to the infant's current behavior.

## REE Relevance

Cleanest dissociation of contingency from content in the infant literature. The infant monitoring system is not responding to what the partner does -- it is comparing the timing of responses against an expected contingency template. This is a temporal prediction error signal, not a feature-matching signal.

For Q-035: the monitoring architecture at 2 months tracks temporal structure of responses (contingency), not semantic content. The same temporal computation will later track rule compliance.

For ARC-049: the bilateral play frame tag requires temporal contingency computation running continuously, operational at 2 months.

## Limitations

- Original study had small N; later replications have mixed fidelity.
- Ecological artificiality of closed-circuit TV setup.
- Some debate about whether the effect reflects contingency detection vs. fatigue.

## Action

Supports Q-035 and ARC-049. Suggests implementation metric: REE frame monitoring should compute temporal prediction error rather than content matching. The double-video paradigm could inspire an REE experiment where an agent responds to a replay of a past partner state -- does frame confidence degrade?
