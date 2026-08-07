# Burda, Edwards, Pathak, Storkey, Darrell & Efros (2019) — Large-Scale Study of Curiosity-Driven Learning

**Claim tested:** MECH-130 — curiosity-driven approach must distinguish world-state novelty from agent-policy novelty.
**Direction:** supports · **Confidence:** 0.68

## What the paper did

This is the scaled-up successor to Pathak et al.'s intrinsic curiosity module. The authors strip the
extrinsic reward out entirely and train agents on prediction error alone across 54 benchmark
environments, including the Atari suite and Super Mario Bros. The headline result is optimistic:
purely curiosity-driven agents do surprisingly well, and the intrinsic objective turns out to be
well aligned with the hand-designed extrinsic rewards of many games. Most of the paper is about
which feature space the prediction error should be computed in — random features are adequate for
many benchmarks, learned features generalise better to novel Mario levels.

The part that matters for us is the last of their three contributions, which they state plainly in
the abstract: "We demonstrate limitations of the prediction-based rewards in stochastic setups." In
the discussion they give the general form of the problem — "If the transitions in the environment
are random, then even with a perfect dynamics model, the expected reward will be the entropy of the
transition, and the agent will seek out transitions with the highest entropy" — and then they take
the field's standard thought experiment and run it for real. They return to their maze, add a
television that changes to a random channel when the agent presses a button, and observe that "the
presence of the TV drastically slows down learning", with the agents only sometimes converging on
the extrinsic reward and only if run long enough.

## What it means for MECH-130

MECH-130's first failure mode is stated as an inference: highest unpredictability means highest
information means strongest approach, so an untyped novelty signal will chronically pull the agent
toward the most opaque — and possibly most dangerous — agent available. This paper is the empirical
version of the middle step of that inference, in the single-agent case. An untyped prediction-error
signal is an entropy-seeker. It does not find what is informative; it finds what is least
modellable, and it does so strongly enough to dominate task behaviour rather than merely colour it.

Two details make the support stronger than a bare "curiosity has a noise problem". First, the
authors' statement is explicitly about a *perfect* dynamics model — so this is not a capacity defect
that a better predictor inside MECH-111 would repair. It is a property of what the reward is
computed over. That is precisely MECH-130's structural point: the fix has to change the signal, not
the model. Second, they took a thought experiment the field had been repeating in the abstract and
made it an experiment, and it behaved as feared. The failure mode is real, not a blackboard worry.

In REE's social tier, an agent that is opaque — because it is adversarial, because its policy is
genuinely complex, or because it is deliberately maintaining surface unpredictability — occupies the
structural position the television occupies in this maze.

## Limitations and caveats

The disanalogy is real and I do not want to bury it, because it is the same disanalogy that the
Schmidhuber entry in this directory turns into an outright objection. A noisy TV is *irreducibly*
random: its prediction error never decays, so it is a permanent attractor for any error-based
signal. Another agent's policy is not like that. It is partially learnable, so a signal keyed on
learning *progress* rather than raw error would eventually detach from it — no source typing
required. That is the strongest available argument that MECH-130's failure mode 1 is already solved
by machinery the field has had since 1991.

It is not a knockdown, and the reason is worth recording: an agent's policy is also *non-stationary*
in a way a TV is not. It changes in response to your behaviour, and it keeps changing. A
learning-progress signal facing a continually shifting but learnable target may find another agent
an *enduring* source of positive progress rather than a decaying one — which would be worse for
MECH-130's concern, not better. Nothing in this paper tests that, because nothing in this paper is
multiagent.

Also absent: any social dimension, any harm or risk dimension, and any test of MECH-130's second
(approach–avoidance oscillation) or third (adversarial exploitation) failure modes. This entry
carries the mechanism only.

## Confidence reasoning

Source quality 0.85 — ICLR 2019, 54 environments, and the noisy-TV result is reproduced and cited
downstream often enough to count as established. Mapping fidelity 0.62 — the mechanism transfers,
the specific attractor does not, and the setting is single-agent. Transfer risk 0.40 — Atari mazes
to a REE social tier is a substantial jump, though the reward formalism is the same object. The
aggregate lands at 0.68, slightly above the component mean, because the authors state the mechanism
in fully general terms rather than as a property of their particular maze, and general statements
travel better than results do.
