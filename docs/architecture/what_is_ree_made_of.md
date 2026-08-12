---
title: What Is REE Made Of?
nav_order: 3
---

# What Is REE Made Of?

<div class="ree-doc-intro">
  <p class="ree-eyebrow">Architecture route</p>
  <p class="ree-doc-lead">Before the differentiated mechanism inventory: a whole-system compression of what REE-v3 actually consists of, mechanically, once "it uses PyTorch" is unpacked into what that does and does not mean.</p>
  <p class="ree-doc-meta">Architecture note. Exploratory research material; no REE work has been accepted for peer-reviewed publication.</p>
</div>

**Status:** architecture note (whole-system presentation framing; not a registered falsifiable claim)  
**Depends on:** five_axioms_foundations.md, overview.md, ethical_agency_derivation.md  
**Source:** reconciled from three independent same-day drafts of this idea, 2026-08-10 —
[docs/thoughts/2026-08-10_ree_as_one_understandable_cognifold.md](../thoughts/2026-08-10_ree_as_one_understandable_cognifold.md)

---

As the architecture becomes more differentiated, it becomes easier to understand any one
mechanism and harder to hold the whole organism in mind. The names of regions, streams,
gates, and experiments can obscure a simpler computational picture underneath them. This
page is that picture, given before the [architecture overview](overview.md) and its inventory
of individual components, not instead of it.

## REE is not "a neural network"

**REE-v3 is not "a neural network." It is a hybrid dynamical system whose changing internal
state is partly represented by PyTorch tensors, whose learned transformations are partly
PyTorch neural networks, and whose remaining machinery consists of explicit memories, gates,
clocks, buffers, search procedures, replay rules, state machines, and update rules.**

PyTorch is better thought of as part of the mathematical tissue REE is built from than as
the cognitive architecture itself. A `nn.Linear(32, 64)` layer is, mechanically, a learned
transformation from 32 numbers to 64 numbers via a matrix of weights and biases; a recurrent
module carries state forward so that the transformation happening now can depend on what
happened before; automatic differentiation lets prediction or task error be traced backward
through these transformations so the learned parameters can change. Saying "REE uses
PyTorch" does not mean REE is one large opaque network. It means PyTorch supplies tensors,
learnable transformations, recurrent modules, and gradient-based learning for the parts of
the architecture where those are the right tool.

A coordinate in one of REE's latent vectors does not intrinsically mean anything
human-readable. `z_world[7] = 0.63` is not itself a symbol like "resource to the
north-east." Meaning arises from how the value was produced, what it covaries with, what it
helps predict, and what downstream mechanisms do with it.

## Four kinds of computational "meat"

A useful whole-system decomposition sorts everything REE is made of into four kinds of
internal substance. Every mechanism documented elsewhere on this site belongs to one of
these four.

**1. Learned structure.** The learned weights and biases inside encoders, predictors,
recurrent networks, scoring heads, and related modules — roughly analogous to acquired
synaptic structure: relatively persistent parameters that determine how one internal state
transforms into another. [E1](e1.md), [E2](e2.md), and parts of [E3](e3.md) contain this
kind of learned structure.

**2. Moment-to-moment activity.** The structured latent state: `z_self`, `z_world`,
`z_beta`, `z_theta`, `z_delta`, and — depending on configuration — dedicated harm,
affective-harm, resource, unpleasantness, interoceptive-distress, blocked-agency, and other
specialised streams. REE does not possess one tensor called "mind"; its immediate state is
already factorised into interacting but bounded streams.

**3. Persistent internal state that is neither immediate activation nor ordinary learned
weights.** Easy to overlook, and plausibly central to understanding REE as a mind-like
dynamical system: recurrent hidden state, [E1](e1.md) context-memory slots, goal attractors
and traces, [residue and valence terrain](residue_geometry.md),
[hippocampal maps and trajectory buffers](hippocampal_systems.md), familiarity state, anchor
sets, staleness and verisimilitude estimates, ghost-goal structures, and commitment state —
quantities that carry the consequences of earlier processing forward through time. Memory is
therefore distributed across several different computational forms at once: some history
lives in learned weights, some in recurrent activation, some in explicit memory structures,
some in residue and valence terrain, some in goals, some in replayable trajectories.

**4. Explicit dynamics — the computational anatomy.** A substantial part of REE is not
learned neural-network tissue at all. The multi-rate clock determines when different
processes update. Theta buffers integrate across rates. The beta gate controls propagation
of committed policy. The [hippocampal system](hippocampal_systems.md) uses explicit
trajectory-search procedures such as the Cross-Entropy Method (CEM). Replay follows explicit
provenance rules, and `hypothesis_tag` is a literal boolean distinction between
simulated/replayed material and realised experience, so hypothetical events cannot write
residue as though they happened. Commitment, release, closure, residue accumulation, and
[neuromodulatory regulation](control_plane.md) contain explicit arithmetic, state-machine, or
gating rules. These mechanisms are part of the mind just as much as the trainable networks
are.

The repository also contains more possible substrate than any one agent configuration
activates. A given run instantiates a configured subset of the available mechanisms — the
cognifold should be understood as the **instantiated dynamical system**, not the union of
every optional mechanism that exists in the repository.

## The whole loop

Viewed at this level, the apparent complexity compresses into a fairly simple recurrent
process:

```text
observation
    |
learned encoders
    |
self / world / affective / temporal / motivational state
    |
E1: what tends to happen?
    |
E2: what would this action do?
    |
hippocampal systems: construct possible trajectories
    |
E3 and associated control systems: evaluate and compare them
    |
commitment / control: does a trajectory propagate into action?
    |
action
    |
actual consequence compared with prediction / counterfactual
    |
latent state + goals + residue + memory + precision + control state change
    |
repeat
```

Offline replay and sleep-like processes then modify some of the persistent structures from
which future waking processing begins. The whole recurrent transformation is the mind, much
more than any one tensor or neural network is.

## REE as a single cognifold

The complete cognifold is broader than the latent `z` state alone. At time `t`, a useful
conceptual compression is:

```text
M_t = { z_t, h_t, H_t, R_t, G_t, C_t ; theta }
```

where `z_t` is current latent activity, `h_t` is recurrent and predictive hidden state,
`H_t` is hippocampal and episodic structure, `R_t` is residue and valence terrain, `G_t` is
goals and motivational state, `C_t` is control, commitment, precision, clocks, gates, and
neuromodulation, and `theta` is learned parameters. The living computational object then
evolves as:

```text
M_(t+1) = F_theta(M_t, observation_t, action_t)
```

with the environment outside that boundary. **The cognifold is not `z_world`, and it is not
even the collection of all the `z` streams. It is the total evolving internal state-space of
the machine, together with the structured transformations that determine how one state
becomes the next.** PyTorch represents and learns parts of that state-space and its
transformations; Python and the explicit algorithms provide the rest; the architecture
specifies which parts may influence which other parts, on what timescale, and under what
conditions.

Seen this way, REE-v3 compresses despite its many mechanisms to:

**a structured state that predicts, imagines, evaluates, commits, acts, remembers the
consequences, and changes the state from which it will do all of those things next time.**

## What this is not

This is a mechanistic explanatory framing, not a claim that REE-v3 is conscious, sentient,
or a moral patient. REE-v3 contains welfare-relevant primitives — harm streams, residue,
suffering-like accumulators, replay — but per the standing non-sentience boundary (SENT-0),
it is not treated as a candidate moral patient, and that boundary is re-evaluated at every
generation boundary rather than assumed permanent.

## Where to go next

This page is a compression, not a replacement for the component documents — each of the four
kinds of computational meat above is implemented by named mechanisms with their own pages:

- [E1 — persistent predictive substrate](e1.md), [E2 — fast forward predictor](e2.md),
  [E3 — trajectory selection and commitment](e3.md)
- [Hippocampal systems](hippocampal_systems.md) — trajectory proposal, map, and replay
- [Residue and valence terrain](residue_geometry.md)
- [Goal state](goal_wanting_signal_chain.md)
- [Control plane](control_plane.md) — precision, commitment, and neuromodulation
- [Sleep / offline integration](sleep.md)
- [Architecture overview](overview.md) — the full component and mechanism inventory
