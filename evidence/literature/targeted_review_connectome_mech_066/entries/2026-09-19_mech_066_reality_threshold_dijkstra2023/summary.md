# Subjective signal strength distinguishes reality from imagination (Dijkstra & Fleming, 2023)

## What the paper did

Dijkstra and Fleming attack a problem that traditional psychology experiments cannot get at: if imagery and perception share neural substrate, what keeps them apart? The methodological obstacle is that participants rapidly learn the structure of the experiment -- once they know real stimuli are sometimes present, their judgements reflect that knowledge rather than the mechanism under study. Their solution is one trial per participant. Each person contributes a single, naive judgement, which is expensive but defeats the learning confound outright.

They contrast two accounts. On the first, the *intention* to imagine is used to identify and discount self-generated signals -- a source-tagging account. On the second, internally generated signals are simply weaker on average, so sensory strength can serve as a proxy for reality. Combining the psychophysics with computational modelling and neuroimaging, the data favour the second: imagined and perceived signals are **intermixed**, and the reality judgement is a threshold on whether the combined signal is strong enough. The authors state the consequence directly -- when imagined or virtual signals are strong enough, they become subjectively indistinguishable from reality.

## Why this is the most discriminating entry in the pull, and why it is `mixed`

MECH-066 is two claims joined by a *but*: channels **may** share representations, **but** must stay separated at durable write boundaries. Almost all the literature bears on one half. This paper addresses both, and reaches a different verdict on each, which is why the blanket direction is `mixed` rather than a compromise between two guesses.

On the permissive half, this is about as strong as support gets. MECH-066's concession that sharing is *permitted* turns out to understate the reference system: it does not merely tolerate sharing, it additively intermixes the two signals with no source tag preserved in the mixture. Whatever MECH-066 gives up by allowing representational overlap, it is giving up nothing biology bothered to keep.

On the restrictive half, the weakening is specific and worth stating precisely. It does not touch the *requirement* -- the reality threshold exists, and it exists because the separation has to be made somehow. What it weakens is the implicit *mechanism*. A threshold on an intermixed signal is a magnitude comparison, and it has an unavoidable false-positive regime. Worse, from a design standpoint, it enters that regime exactly when the internally generated signal is most vivid. That is the least convenient possible correlation for anything functioning as a write gate: it leaks hardest when the simulation is most confident, which is when a planning system is doing its most consequential work.

The second finding is the one I would flag hardest for REE. The intention-to-imagine account -- roughly, *I know I generated this, so I will handle it correctly* -- is the account the data **do not** support. An architecture that leaned on a self-generated flag as its discriminator would be assuming a mechanism the reference system appears not to use.

## What this actually implies for REE

Read carefully, this is a warning against a simplification rather than a challenge to what REE currently does. REE's separation is typed in code: `update_residue` accepts only post-commit harm, `compute_prediction_loss` trains E1 only on actual observations. Nothing in REE infers channel identity from signal magnitude, and nothing relies on an intention flag. So the paper's negative results land on designs REE has not adopted.

Where it has teeth is prospectively. If a future substrate change were to route pre-commit and post-commit error through a shared magnitude-weighted pathway -- which is the natural, efficient thing to do once the representations are shared anyway -- this paper predicts the failure mode and predicts that it will be invisible under weak-simulation test conditions. That is the third failure signature, and it is the kind that passes every test written before the capability exists.

## Limitations

The locus is a readout, not a write. A reality *judgement* is a decision about whether a stimulus was present; MECH-066 is about what reaches persistent state. The extension from one to the other is mine, not the paper's.

There is also an asymmetry of purpose that I think is genuinely load-bearing and not just a caveat for form's sake. The human visual system is not trying to keep imagery out of a durable store. Its problem is online scene interpretation, where a strength threshold may be an excellent solution. REE's problem -- keeping simulated error out of the residue field -- is a different problem, and the reference system's design choice may simply be inapplicable rather than instructive. This cuts *against* reading the weakening too strongly: that biology uses a fallible threshold is not an argument that REE should, nor that REE's stricter typed boundary is over-engineering.

Finally, one trial per participant is what makes the result credible and also what limits it: every inference is between-subject, with no within-subject replication available by construction.

## Confidence

0.72, the second-highest in this pull, which may look odd for an entry that partly weakens the claim. The reason is that confidence here rates the quality of the *linkage*, not the comfort of the conclusion. This paper addresses MECH-066's two halves separately and discriminates between two competing mechanisms with a design built specifically to make that discrimination possible. That is more informative than a higher-confidence entry that supports the claim vaguely.
