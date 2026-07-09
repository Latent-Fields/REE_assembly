# Schmidhuber (2010) — Formal Theory of Creativity, Fun, and Intrinsic Motivation (1990–2010)

**Claims tested:** MECH-314c (primary), MECH-314, ARC-065
**Direction:** mixed · **Confidence:** 0.70

## What the paper did

Schmidhuber reviews two decades of his own program formalising intrinsic motivation as
**compression progress**. The core object is a predictor/compressor of the agent's sensory
history plus a *separate* reinforcement-learning controller whose reward is the *improvement*
in that compressor — the number of bits saved in encoding the history before versus after a
learning step. "Interesting" data is data of *intermediate* compressibility: neither already
compressed (boring, known) nor incompressible (random, unlearnable). The controller is thus
driven to act so as to generate observations that let the model get better. Schmidhuber then
makes the sweeping move that this single drive explains curiosity, creativity, science, art,
music, and humour — all reframed as the pursuit of novel, better-compressible regularity.

## The finding that matters for REE

Two things carry over. First, this is the information-theoretic form of **MECH-314c**: reward
the *derivative* of model quality, not its level. REE's `|PE_t − PE_{t−K}|` learning-progress
bonus and Schmidhuber's `bits_before − bits_after` are the same idea in two currencies, and
Schmidhuber (1991) is one of the two references already named inside the MECH-314c claim. That
lineage makes this a genuine grounding source. Second, the "intermediate compressibility"
criterion gives a concrete tuning target: the bonus should peak on partially-learned structure,
which is exactly the anti-noisy-TV property Oudeyer & Kaplan also demand.

## Why the direction is *mixed*, not supporting

Schmidhuber's framing is a clean instance of the design REE deliberately argues *against*.
Everything is one scalar reward maximised by one controller over one world model. REE's
ARC-021 / MECH-069 commitment is the opposite — three incommensurable channels (viability,
social, epistemic) that must not be collapsed to a single number. So REE can legitimately
import the compression-progress *signal for the epistemic channel*, but importing
Schmidhuber's *objective* would contradict the architecture's load-bearing claim. This entry
is therefore both supporting evidence for MECH-314c and a documented counter-example REE's
single-functional critique should cite by name.

The second, more operationally important departure: compression progress rewards improving the
**world model** (knowledge-based IM). Skills, Schmidhuber concedes, are acquired only as a
*by-product* of seeking compressible data. That is precisely the pattern WS-1 is staring at —
the curiosity substrate is wired, yet foraging competence is still zero, because a
knowledge-based drive does not *directly* reward crossing a behavioural goal-achievement floor.
This is the seam where Baldassarre & Mirolli's competence-based IM (companion entry) does the
work Schmidhuber's theory cannot.

## Limitations and caveats

The single-scalar objective is also a wireheading surface: an agent free to choose its own
data can drift toward observations it can *trivially* make more compressible, so the theory
leans on the environment to keep supplying genuinely novel learnable regularity. And the
compression-progress estimate is noisy in high-dimensional stochastic input — REE's Phase-1
broadcast-scalar proxy would inherit that noise. Net: strong lineage grounding for MECH-314c's
signal, an explicit exhibit for REE's anti-single-functional argument, and a clear pointer that
knowledge-based IM alone will not lift the competence floor.
