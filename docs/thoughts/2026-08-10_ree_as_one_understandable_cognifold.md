# Thought Intake: REE as one understandable cognifold

Status: processed
Intake: evidence/planning/thought_intake_2026-08-10_ree_as_a_single_understandable_cognifold.md
Processed in:
- No claims.yaml entry: this is a documentation/public-communication proposal, not a
  falsifiable empirical claim. See Stage 2 intake.
- Canonical draft of a three-way duplicate: the same idea was independently written up
  three times (this file; 2026-08-10_ree_as_single_understandable_cognifold.md;
  2028-08-10_REE_as_a_single_understandable_cognifold.md, whose year is a typo for 2026).
  This file (most complete: explicit "Possible affected components" section) is treated as
  canonical; the other two are marked superseded, pointing here.
- Follow-on chipped: writing the actual public-facing page is tracked as a separate task,
  not performed as part of thought intake.

Date: 2026-08-10
Source: discussion of what mechanically constitutes REE-v3 when the environment is excluded
Purpose: preserve a whole-system explanatory framing and propose that it become prominent in the public-facing REE material

---

## Core thought

My vision for REE is ultimately one single understandable cognifold.

As the architecture has become more differentiated, it has become easier to understand individual mechanisms while simultaneously becoming harder to hold the whole organism in mind. The names of regions, mechanisms, streams, gates and experiments can obscure a simpler computational picture underneath them.

A useful description is:

**REE-v3 is not “a neural network”. It is a hybrid dynamical system whose changing internal state is partly represented by PyTorch tensors, whose learned transformations are partly PyTorch neural networks, and whose remaining machinery consists of explicit memories, gates, clocks, buffers, search procedures, replay rules, state machines and update rules.**

PyTorch is therefore better thought of as part of the mathematical tissue from which REE is built, rather than as the cognitive architecture itself.

This distinction feels important both for understanding the implementation and for explaining REE to somebody encountering it for the first time.

---

## What the “meat of the mind” is mechanically

At the most concrete level, much of REE’s moment-to-moment internal activity is represented as arrays of floating-point numbers: PyTorch tensors.

In the current default latent stack, the core immediate state includes approximately:

- `z_self`: 32 numbers — self/body-related state;
- `z_world`: 32 numbers — world-related state;
- `z_beta`: 64 numbers — shared affective/integrative state;
- `z_theta`: 32 numbers — temporal/sequence context;
- `z_delta`: 32 numbers — slower regime/motivational context.

That is 192 floating-point values before the optional specialised channels are included. Current REE-v3 can additionally carry dedicated harm, affective-harm, resource, unpleasantness, interoceptive-distress, blocked-agency, suffering and other specialised states depending on configuration.

A coordinate in one of these vectors does not intrinsically mean something human-readable. `z_world[7] = 0.63` is not itself a symbol such as “resource to the north-east”. Meaning arises from how the value was produced, what it covaries with, what it helps predict, and what downstream mechanisms do with it.

A PyTorch layer such as `nn.Linear(32, 64)` is, mechanically, a learned transformation from 32 numbers to 64 numbers using a matrix of weights and biases. A Rectified Linear Unit (ReLU) introduces non-linearity. A Long Short-Term Memory (LSTM) network adds recurrent state so that the transformation occurring now can depend on what happened previously. PyTorch automatic differentiation then allows prediction or task error to be traced backwards through these transformations so that the learned parameters can be changed.

This means that “REE uses PyTorch” does **not** mean that REE is one large opaque neural network. It means that PyTorch provides tensors, learnable transformations, recurrent modules and gradient-based learning for those parts of the architecture for which those are appropriate.

---

## Four kinds of computational “meat”

A useful whole-system decomposition is into four kinds of internal substance.

### 1. Learned structure

These are the learned weights and biases inside encoders, predictors, recurrent networks, scoring heads and related modules.

They are roughly analogous to acquired synaptic structure: relatively persistent parameters that determine how one internal state is transformed into another. E1, E2, parts of E3, the latent encoders and many specialised heads contain this kind of learned structure.

### 2. Moment-to-moment activity

This is the structured latent state: `z_self`, `z_world`, `z_beta`, `z_theta`, `z_delta`, specialised harm/resource/affective streams, precision values and other currently active signals.

REE therefore does not possess one tensor called `mind`. Its immediate state is already factorised into interacting but bounded streams.

### 3. Persistent internal state that is neither immediate activation nor ordinary learned weights

This category is easy to overlook but may be central to understanding REE as a mind-like dynamical system.

It includes recurrent hidden state, E1 context-memory slots, goal attractors and traces, residue fields, hippocampal maps and trajectory buffers, valence vectors, familiarity state, anchor sets, staleness and verisimilitude estimates, ghost-goal structures, commitment state and other quantities that carry the consequences of earlier processing forward through time.

Memory is therefore distributed across several different physical/computational forms. Some history is stored in learned weights; some in recurrent activation; some in explicit memory structures; some in residue and valence terrain; some in goals; some in replayable trajectories.

### 4. Explicit dynamics — the computational anatomy

A substantial part of REE is not learned neural-network tissue at all.

The multi-rate clock determines when different processes update. Theta buffers integrate across rates. The beta gate controls propagation of committed policy. The hippocampal system uses explicit trajectory-search procedures such as the Cross-Entropy Method (CEM). Replay follows explicit provenance rules. `hypothesis_tag` is a literal Boolean distinction between simulated/replayed material and realised experience so that hypothetical events cannot simply write residue as though they happened. Commitment, release, closure, residue accumulation, neuromodulatory regulation and many other mechanisms contain explicit arithmetic, state-machine or gating rules.

These mechanisms are part of the mind just as much as the trainable neural networks are.

The repository also contains more possible substrate than every individual agent configuration activates. A particular REE-v3 run instantiates a configured subset of the available mechanisms. The cognifold should therefore be understood as the instantiated dynamical system, not merely as the union of every optional mechanism that exists in the repository.

---

## The whole loop

Once the implementation is viewed at this level, the apparent complexity compresses into a fairly simple recurrent process:

```text
observation
    ↓
learned encoders
    ↓
self/world/affective/temporal/motivational state
    ↓
E1: what tends to happen?
    ↓
E2: what would this action do?
    ↓
hippocampal systems: construct possible trajectories
    ↓
E3 and associated control systems: evaluate and compare them
    ↓
commitment/control: does a trajectory propagate into action?
    ↓
action
    ↓
actual consequence compared with prediction/counterfactual
    ↓
latent state + goals + residue + memory + precision + control state change
    ↓
repeat
```

Offline replay and sleep-like processes then modify some of the persistent structures from which future waking processing begins.

The important point is that **the whole recurrent transformation is the mind much more than any one tensor or neural network is**.

---

## REE as a single cognifold

The complete cognifold should probably be conceived more broadly than the latent `z` state alone.

At time `t`, a useful conceptual compression is:

```text
M_t = { z_t, h_t, H_t, R_t, G_t, C_t ; θ }
```

where:

- `z_t` = current latent activity;
- `h_t` = recurrent and predictive hidden state;
- `H_t` = hippocampal and episodic structures;
- `R_t` = residue and valence terrain;
- `G_t` = goals and motivational state;
- `C_t` = control, commitment, precision, clocks, gates and neuromodulation;
- `θ` = learned parameters.

Then the living computational object can be thought of as something like:

```text
M_(t+1) = F_θ(M_t, observation_t, action_t)
```

with the environment outside that boundary.

This suggests a particularly useful formulation:

**The cognifold is not `z_world`, and it is not even the collection of all the `z` streams. It is the total evolving internal state-space of the machine, together with the structured transformations that determine how one state becomes the next.**

PyTorch provides a way to represent and learn parts of this state-space and its transformations. Python and the explicit algorithms provide other dynamics. The architecture specifies which parts may influence which other parts, on what timescale, and under what conditions.

Seen this way, REE-v3 can be described very simply despite its many mechanisms:

**a structured state that predicts, imagines, evaluates, commits, acts, remembers the consequences, and changes the state from which it will do all of those things next time.**

That may be one of the clearest routes to the original ambition of a single understandable cognifold.

---

## Proposal: make this prominent in the public-facing REE pages

This whole-system description should probably be placed somewhere prominent in the public-facing web material, rather than left implicit across component pages.

As REE accumulates differentiated mechanisms, a new reader can increasingly learn the organs without ever seeing the organism. The public pages currently have strong explanations of the derivation, named components and individual architecture, but the bridge from “this repository uses PyTorch” to “this is what the internal computational object actually consists of” is not obvious.

A short public section or dedicated page could be titled something like:

- **What is REE made of?**
- **REE as a cognifold**
- **The REE mind in one picture**
- **What is actually running inside REE?**

It should probably appear very early in the reader journey — potentially linked from the home page and placed near the top of the architecture overview — before a reader is asked to understand the growing inventory of mechanisms.

The public explanation should contain:

1. the statement that REE is a hybrid dynamical system rather than one neural network;
2. a plain-language explanation of tensors, learned weights and PyTorch;
3. the distinction between learned structure, current latent activity, persistent internal state and explicit dynamics;
4. the simple recurrent loop from observation through prediction, imagination, commitment, action and memory;
5. the compact `M_t` cognifold formulation;
6. a statement that optional/configuration-gated mechanisms are not all active in every run;
7. an explicit research-status boundary: this is a mechanistic explanatory framing and **not** a claim that REE-v3 is conscious, sentient or a moral patient.

This seems consistent with the existing public-information principle of **overview before inventory**, and with the existing architecture-overview language that REE remains a coherent single cognifold. It may provide the missing conceptual layer between that claim of unity and the increasingly detailed mechanism map.

The goal would not be to simplify REE by hiding complexity. It would be to make the complexity navigable by giving the reader a stable whole into which each later mechanism can be placed.

---

## Possible affected components / documentation

- L-space / latent stack
- E1 persistent predictive substrate
- E2 fast forward prediction
- E3 trajectory selection and commitment
- hippocampal memory, trajectory proposal and replay
- residue and valence terrain
- goal state
- control plane, precision and commitment gates
- sleep/offline integration
- public home page / reader orientation
- architecture overview and system map
- Development Map / public visual explanation
- Brain Map and Code Atlas as possible deeper routes from the whole-system picture
