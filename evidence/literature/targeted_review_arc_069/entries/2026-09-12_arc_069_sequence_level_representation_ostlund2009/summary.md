# Ostlund, Winterbauer & Balleine 2009 -- a biological ARC-069-OFF control

Ostlund and colleagues lesioned dorsomedial prefrontal cortex in rats and ran them on a concurrent
bidirectional heterogeneous chain task, where which reward arrived depended on the order in which
two lever presses were made. Both lesioned and sham animals learned the task. The dissociation
appeared in the probe tests. When an outcome was devalued, or its contingency degraded by delivering
it non-contingently, sham rats withheld the *whole sequence* that had earned it. Lesioned rats did
not reorganise at that level at all: they withheld only the terminal response, the press closest to
the devalued outcome, leaving the more distal press intact. They were representing the elements as
separate behavioural units where the shams were representing a sequence.

I include this entry mainly because of what the lesion group *is*. ARC-069's own falsifiable
prediction is that an agent lacking the regranularisation substrate, run for many episodes on a
repeating task, will still be proposing at single-action grain at episode 1000 and paying the full
combinatorial cost. The dmPFC-lesioned rat is that agent, in biology, and it is otherwise competent
-- it learns the task, it chooses correctly on value and on discriminative stimuli. What it has lost
is specifically the coarser grain. That tells us something ARC-069 asserts but has never had
evidence for: the coarse grain is not an automatic consequence of practice. It has a dedicated
dependency, and removing that dependency leaves an agent permanently stuck fine. If regranularisation
were emergent from training alone, this dissociation should not exist.

The mapping problem here is the largest in this pull and I do not think it should be smoothed over.
Outcome devaluation reads out the grain of the *action-outcome representation used for goal-directed
control* -- the units over which value is assigned. ARC-069 concerns the units the hippocampal
proposer emits into rollout and that ARC-062 apprehends rules over. For most architectures one might
wave a hand and say these are the same representation seen from different angles. We cannot, because
ARC-007 proposals are explicitly committed to being value-flat. A result about the grain of
value-assignment therefore has no guaranteed purchase on the grain of a value-flat proposal stream.
This is precisely the kind of gap that looks like a technicality until an experiment is designed on
the assumption it does not exist.

The chain is also only two presses deep. At that depth the result cannot distinguish a system with
one optional coarser grain from a system that rescales grain continuously, and ARC-069 is the second.
And because the lesion is permanent and the test is post-training, nothing here speaks to whether
grain can move *back* -- the ARC-070 direction is untouched.

Confidence 0.66, the lowest of the three ARC-069 entries. Source quality 0.85: clean design, Balleine
lab, well cited. Mapping fidelity 0.65 is doing the work of the discount, for the value-grain versus
proposal-grain reason above; transfer risk 0.40. Strong evidence that policy grain is a real and
dissociable architectural variable; weak evidence that it is the variable ARC-069 names.
