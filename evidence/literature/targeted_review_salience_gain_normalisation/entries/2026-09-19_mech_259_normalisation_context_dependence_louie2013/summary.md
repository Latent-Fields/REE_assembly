# Normalization is a general neural mechanism for context-dependent decision making (Louie, Khaw & Glimcher, 2013)

## Why this entry exists

A literature pull that returned only the case *for* divisive normalization would be doing advocacy,
not evidence. This is the counterweight, and it comes from the same laboratory that supplied the
strongest supporting entry -- which is the best kind of counterweight, because it is not a rival
school scoring a point.

Louie, Khaw and Glimcher take the normalization equation that describes LIP value coding and ask
what it does to *behaviour* when it sits inside a choice model. The answer is that it produces
classically irrational phenomena: choice probabilities that depend on the values of irrelevant
alternatives, and on the sheer number of alternatives present. They then find these effects
empirically in both monkey and human value-guided choice.

## The bearing on the substrate decision

SD-032a's coordinator ends in a softmax over four operating modes. That is a stochastic discrete
choice, formally the same object Louie et al. are modelling. Their result says: if the quantities
entering that softmax are divisively normalized against a pool, then the probability assigned to
`external_task` becomes a function of how loudly the other modes are arguing, not just of its own
evidence. Under today's independent per-signal clamp there is no such leak.

Three consequences deserve to be on the record before anyone builds.

The first is a forward compatibility hazard that is easy to miss. MECH-261's own notes anticipate a
fifth operating mode -- `parallel_goal_deliberation`, in V4, once SD-033e lands -- and specify that
`operating_mode_vector` be a dictionary so the mode can be added without schema churn. Under a
normalizing operator, adding that fifth key would change the probabilities of the existing four even
with every input unchanged. The number-of-alternatives effect is not a curiosity in this paper; it
is one of its two headline findings. A schema designed for painless extension would acquire a
silent numerical dependence on extension.

The second is an interaction with MECH-266. The context effects Louie et al. report are largest when
option values are close -- the near-indifference regime. That is precisely the regime MECH-266's
asymmetric hysteresis exists to stabilise. A normalizing operator amplifies sensitivity to the
competing set near indifference while a Schmitt trigger suppresses switching there. They are not
obviously incompatible, but nobody has asked whether they compose, and MECH-266 is currently
`provisional` with zero experimental entries.

The third is epistemic. If REE adopts normalization and later observes context-dependent mode
occupancy, that finding would be a *confirmed prediction of the operator*, not a substrate
pathology. Unless the operator is registered as the expected cause in advance, a whole class of
future occupancy anomalies becomes uninterpretable.

## What I am careful not to import

"Irrational" is a normative verdict about a chooser with preferences. REE's coordinator is not
choosing between goods; it is assigning an internal operating mode, and there is no axiom of
revealed preference to violate. The transferable content is the weaker structural claim --
normalization makes the outcome depend on the composition of the alternative set -- and that is what
I have mapped. Carrying the rationality framing across would be the same category error the autopsy
warned about, just in the opposite direction.

## Confidence

0.72, direction mixed. The study is strong and the structural lesson transfers cleanly. The discount
is for the fact that REE would be drawing an inference about a mechanism it has not adopted, in a
setting with no chooser and no reward.
