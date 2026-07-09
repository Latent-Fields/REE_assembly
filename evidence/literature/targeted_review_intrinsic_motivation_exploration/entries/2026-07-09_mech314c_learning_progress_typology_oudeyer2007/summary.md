# Oudeyer & Kaplan (2007) — What is Intrinsic Motivation? A Typology of Computational Approaches

**Claims tested:** MECH-314c (primary), MECH-314, ARC-065
**Direction:** supports · **Confidence:** 0.82

## What the paper did

Oudeyer & Kaplan set out to end the terminological fog around "intrinsic motivation" by
building a *formal* typology inside the reinforcement-learning reward framework. Every
intrinsic-motivation system, they argue, is a particular choice of an internally-computed
reward `r_t` that depends not on task payoff but on the agent's own predictive/knowledge
state. They then partition the space of such rewards into families: novelty-based,
prediction-error / surprise-based, predictive-information / information-gain-based, and —
the one they press hardest — **learning-progress-based** motivation. The companion
engineering paper (Oudeyer, Kaplan & Hafner 2007, *IEEE Trans. Evolutionary Computation*)
gives the worked algorithm, IAC / R-IAC, and the Playground Experiment: a physical robot on
a baby-mat that, driven only by learning progress, spontaneously organises its own behaviour
into ordered developmental stages (first mouthing, then touching, then vocalising) with no
externally specified curriculum.

## The finding that matters for REE

The load-bearing result is a *dissociation between three candidate signals*. Maximizing
**novelty or prediction error** (roughly MECH-314a) pulls the agent toward maximally
*unpredictable* regions — which in any stochastic world means the white-noise / "noisy TV"
trap, where error stays pinned high precisely because nothing is learnable. Maximizing
**predictability** (the mirror-image objective) collapses the agent onto already-mastered,
trivial regions. Only the **first derivative** — the *rate of reduction* of predictive
error, i.e. learning progress — is stable: it is near-zero both where the agent already
knows everything and where it can never learn anything, and it peaks exactly in the
"zone of proximal development" the agent is currently mastering. That derivative is the
signal REE registered as **MECH-314c**, and this paper is its direct ancestor and namesake.

## Why this feeds WS-1 (capability floor) and the goal pipeline

WS-1's problem is an agent that cannot forage: structure was specified faster than
capability was earned. Oudeyer & Kaplan describe the mechanism by which capability is
*earned* rather than assumed — an agent with no competence and no external reward will,
under a learning-progress drive, self-generate a curriculum that walks it up the competence
ladder one masterable sub-task at a time. This is the developmental-robotics answer to the
Bitter Lesson bite in WS-6: not "hand-specify the skill" and not "scale until it appears,"
but "install the drive that makes the agent build its own curriculum." For the goal pipeline
this reframes *wanting*: a learning-progress bonus is a **wanting signal indexed to
competence gain**, distinct from the hedonic/homeostatic wanting SD-012/MECH-229 already
model. It suggests the goal pipeline's missing ingredient may be a drive that wants
*getting-better-at-a-goal*, not only the goal's consummation.

## Limitations and the honest caveat

The mapping is architecture-to-architecture within a shared RL formalism, which keeps
transfer risk low — but the fidelity ceiling is real. Oudeyer & Kaplan compute learning
progress **per region** of a partitioned sensorimotor space (R-IAC recursively splits the
space and meta-predicts error-reduction in each), and that regional structure is what
produces the developmental curriculum. REE's Phase-1 MECH-314c is a single **broadcast
scalar** (a global running-variance derivative) applied identically to all K action
candidates; it can nudge overall exploration but cannot yet build the per-region curriculum
that gives the result its teeth. So this is strong support for the *claim that learning
progress is the correct competence-earning signal* and a clear motivation for a
per-candidate / per-region Phase-2 upgrade — it is **not** evidence that the current
substrate already realises autonomous developmental staging. That gap is precisely what a
WS-1 competence experiment should target.
