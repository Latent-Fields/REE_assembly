# Orseau & Armstrong (2016) -- Safely interruptible agents

**Claim tested:** ARC-098 (safety.autonomy_suspension_without_shame) | **Direction:** supports | **Confidence:** 0.74

## What the paper did

Orseau (DeepMind) and Armstrong (FHI) address a problem that any containment surface has to answer.
If a human operator can interrupt a learning agent's harmful actions, and those interruptions cost
the agent expected reward, then the agent has an incentive to learn to prevent the interruptions --
by disabling the channel, by avoiding the states that trigger it, or by acquiring a policy that
keeps the operator's hand away from the switch.

They give a formal definition of safe interruptibility: repeated interruption does not change the
agent's learned optimal policy, and gives it no incentive either to prevent or to induce being
interrupted. They then prove that the property is cheaply available. Off-policy learners such as
Q-learning already have it, because the learning update does not condition on the behaviour policy
that the interruption perturbs. On-policy learners such as Sarsa do not, but can be modified to have
it. And even idealised uncomputable agents in deterministic general computable environments can be
made safely interruptible. The paper is one of the foundational technical results in the corrigibility
literature.

## How this bears on ARC-098

ARC-098's first conjunct says a dangerous-self-state detector may suspend autonomy. The obvious
objection to any such surface is the one above: a learning system will treat the suspension as a cost
and route around it. This paper shows the objection is answerable in principle -- there is a formal
property that makes an agent indifferent to the interruption channel, and common learning algorithms
either have it already or can be given it cheaply.

For REE that converts "suspend autonomy" from an aspiration into a design target with a known
technical shape, and it tells the V5 self-model work something concrete about which class of learning
rule keeps a containment surface honest. It is also the only entry in this pull that requires no
cross-species or cross-population inference: the subject *is* an artificial learning agent's
relationship to an externally triggered autonomy suspension, which is ARC-098's first conjunct almost
verbatim. That is why its confidence exceeds the empirically stronger Tangney entry despite being
theory rather than measurement.

## Where the claim outruns the result -- the interesting part

ARC-098 has three conjuncts: suspend autonomy, preserve evidence, seek correction, without global
self-condemnation. This paper covers one of them, and the gap is worth stating precisely because it
is where the claim is actually novel.

Safe interruptibility as defined delivers *indifference*. The agent neither resists interruption nor
courts it. ARC-098 asks for more: an agent that actively seeks correction. Indifference is strictly
weaker, and an indifferent agent satisfies the containment conjunct while failing the corrective one.
So this result is a floor for ARC-098, not a solution to it -- and reading it as support for the
whole claim would paper over the conjunct REE has the least evidence for.

The framework also says nothing at all about preserving evidence. An agent can be perfectly safely
interruptible and still fail ARC-098 by discarding the state that would let an operator diagnose why
the interruption was warranted. Interruptibility governs the agent's incentives around the off
switch; it does not govern its record-keeping. Those are separable properties and ARC-098 asks for
both.

## Limitations

This is a theoretical result about idealised agents, not a demonstration in any deployed system, and
the proofs live in settings that do not match REE's architecture: tabular off-policy reinforcement
learning, and deterministic general computable environments. The stochastic general case is not
covered, so the strongest form of the guarantee does not extend to the settings most like a realistic
deployment. Treating this as evidence that REE's containment surface will be safe would be an
overreach; it is evidence that the property is coherent and achievable in some agent classes, which
is the modest thing ARC-098 needs at this stage.

Two constraints are worth recording as design facts rather than caveats. First, the guarantee depends
on off-policy learning -- an architecture built on on-policy or model-based planning inherits no such
guarantee, and REE's substrate is not obviously in the covered class. That is a live constraint on
the V5 build, not a footnote. Second, subsequent work in this literature has found safe
interruptibility harder in multi-agent and learned-reward settings than the single-agent case
suggests, which matters because ARC-098's sibling claims put the V5 self-model in a social context.

## Confidence reasoning

Source quality strong for its type (0.85): UAI is competitive, the result is foundational and widely
built upon, but it is formal work with no measurement, so it is capped below the empirical entries.
Mapping fidelity high (0.78) -- the paper's subject is almost exactly the claim's first conjunct --
docked for covering one conjunct of three and for delivering indifference where the claim wants
active correction-seeking. Transfer risk is the lowest in this pull (0.25): only the gap from
idealised agent classes to REE's eventual substrate, no cross-domain inference. Aggregate 0.74.
