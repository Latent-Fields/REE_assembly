# A common habit bias across disorders of compulsivity (Voon et al., 2015)

## What the paper did

Voon and colleagues ran the two-step sequential decision task -- the standard instrument for
separating model-based from model-free control -- across three clinical groups chosen because
they share compulsivity rather than because they share a diagnosis: obsessive-compulsive
disorder, binge eating disorder, and methamphetamine use disorder. All three showed the same
shift toward model-free control. They then related the degree of that shift to structural
MRI, and found it tracked lower gray matter volume in caudate and medial orbitofrontal
cortex.

## What it gives MECH-080

Arm 3 of MECH-080 nominates a specific dependent variable: repeated obsolete actions after
reversal. This paper supplies external grounding for that DV in the target population and
does so transdiagnostically, with a convergent anatomical correlate. Model-free dominance is
what insensitivity to contingency change looks like when you measure it properly, and OCD has
it. If the question is whether MECH-080's arm-3 *measurement* is measuring something real in
the disorder it is pointed at, the answer here is yes.

There is a practical bonus. REE can already score this one. The causal grid world carries
`world_rule_shift_enabled` / `_interval` / `_depth`, scoped to `action_map`, which applies
action-pair transpositions and emits `steps_since_world_rule_shift`. Perseveration after a
contingency reversal is therefore instrumentable in V3 today, which is not true of the other
two arms' DVs. That does not unblock the claim -- arm 3 has no manipulation lever, which is
why the experimental proposal was blocked -- but it narrows what is missing to the lever
rather than the readout.

## The mechanism problem, which is the real content of this entry

MECH-080 says OCD is attractor lock-in: an abnormally deep basin in the hippocampal rollout
map, such that normal signals cannot trigger basin exit. That is a claim about pathology
*inside* forward search. The rollout still runs; it just falls into the same well every time.

Voon et al. describe something architecturally opposite. Model-free dominance is not a deep
basin within the planner. It is control being handed to a system that does not plan at all.
On that account the compulsive act is not the output of a forward search that keeps landing
in one place -- it is the output of a cached stimulus-response policy that was never a
forward search in the first place.

Both accounts predict the same behaviour. That is exactly the problem, and it is a problem
for the experiment rather than for the paper. An arm-3 result in REE that scores only
`steps_since_world_rule_shift` would be satisfied equally by a deep-basin agent and by an
agent whose rollout had quietly stopped contributing to action selection, and the second is
the more likely failure mode in a substrate with a known conversion ceiling. Whoever
eventually designs the arm-3 experiment needs a second measurement -- is the rollout still
running and still coupled to the policy -- or the DV will not discriminate the claim from its
main rival.

## Confidence

0.60, `supports`. The direction is `supports` because the behavioural prediction MECH-080
makes is the one the paper observes, in the right population, robustly. Mapping fidelity at
0.50 carries the rival-mechanism problem and is where a reader should look; I considered
`mixed` and decided against it, because the paper does not find anything contrary to the
claim's prediction -- it offers a different explanation for the same finding, which is a
mapping issue rather than a mixed result. The transdiagnostic breadth cuts both ways: it
strengthens the finding and weakens the claim's implicit assumption that this phenotype
picks out OCD specifically.
