# Empowerment as reachable-future-option maximization (Klyubin, Polani & Nehaniv 2005)

## What the paper did

Klyubin, Polani and Nehaniv introduced *empowerment*: the channel capacity -- the maximal mutual information -- between an agent's sequence of actions and the sensory states those actions can later produce. Read plainly, empowerment measures how many distinguishable futures an agent can *reach and tell apart* by its own choosing. It is deliberately goal-independent: no reward function, no task, just a scalar that is high when the agent sits in a richly controllable region of its state space and low when it has painted itself into a corner. The accompanying behavioral prescription is the paper's title -- *all else being equal, be empowered* -- i.e. when nothing else discriminates between options, prefer the one that keeps the larger, more controllable set of futures open.

## Why it is relevant to MECH-454

MECH-454 says E3 today scores harm, benefit, goal, residue and the modulatory stack, but nothing represents the *option-value / reversibility* of an action for the agent's OWN reachable futures. REE's irreversibility-awareness is entirely harm-scoped (residue cannot be erased; No-Go gates; INV-026's foreclosure-of-others). Empowerment is, to my reading, the cleanest existing formalization of exactly the missing quantity: a number that goes *down* precisely when an action cheaply forecloses the agent's own reachable-option space. If you wanted to give E3 the magnitude of a self-directed foreclosure cost, the drop in post-action empowerment is a defensible place to read it from.

## The honest limit of the mapping

But empowerment supplies only *one half* of MECH-454, and not the half that makes the claim novel. Empowerment is an unconditional maximization *drive*; MECH-454 is a conditional *cost* sitting alongside harm/benefit/goal inside a single trajectory score, firing with z_harm below threshold. More decisively, empowerment carries no uncertainty-gating. MECH-454's defining move -- inherited and generalized from DR-12's prediction-error-conditioned E3 confidence -- is that the foreclosure penalty should scale with *how uncertain the forecast is that justifies the foreclosure*: weigh it heavily when the agent is guessing, not at all when it is confident. Empowerment weighs option-preservation identically in both cases. That is, an agent built on empowerment alone would exhibit precisely the "deranged gating" failure mode the claim names (context-insensitive preservation), and an unconditional empowerment maximizer tends toward the *opposite* pole from the one that surfaced MECH-454 -- it hoards options and refuses necessary irreversible action, rather than committing prematurely.

## Distinctions worth keeping straight

Empowerment is not MECH-314 (a curiosity/novelty *bonus* that rewards visiting prediction-error-rich states -- a reward, not a foreclosure cost), and it is not ARC-068 (opportunity cost of *time*, not of option-*space*). It is a conceptual cousin of the Niv opportunity-cost line (ARC-066/MECH-320), which I note as a cross-reference rather than pull here.

## Confidence reasoning

I set confidence at 0.62, dominated by mapping_fidelity rather than source_quality. Source quality is high -- this is the canonical, durable origin of a construct that has survived two decades of intrinsic-motivation research. But for an architectural claim the question is how faithfully MECH-454 maps onto what the paper actually offers, and the answer is: cleanly for the reachable-option-preservation *component*, not at all for the cost-term framing or the uncertainty-gate. This entry is therefore best read as evidence that the *pieces* of MECH-454 are real and formalizable in the literature, while the synthesis -- an uncertainty-gated self-foreclosure cost inside an ethics-engine selector -- remains REE-novel.
