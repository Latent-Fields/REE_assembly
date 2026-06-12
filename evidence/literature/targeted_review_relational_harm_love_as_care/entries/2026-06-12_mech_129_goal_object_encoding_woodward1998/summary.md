# Infants selectively encode the goal object of an actor's reach (Woodward 1998)

**Claim:** MECH-129 (harm-to-agency as a relational signal distinct from harm-to-agent)
**Direction:** supports · **Confidence:** 0.72 · **Class:** behavioral_human

## What the paper did

Woodward used the visual-habituation paradigm to ask a deceptively simple question: when an
infant watches someone reach for one of two toys, what does the infant take the event to be
*about* -- the path the arm travelled, or the object it was reaching for? After habituating to a
reach toward one toy, the toys' positions were swapped and infants saw either a *new-path /
same-goal* reach or a *same-path / new-goal* reach. Nine-month-olds (and, more weakly,
five-to-six-month-olds) dishabituated to the change of goal object, not to the change of path.
The control is the load-bearing part: when an inanimate object of the same dimensions as the
arm touched the toy, infants showed no such selectivity. The goal-encoding is gated on the
event being an *agentive* reach, not on spatial contiguity.

## Why it matters for MECH-129

MECH-129 asserts that in a multiagent world harm must be represented as two distinct signal
types -- harm-to-agent (a cost localised to one's own sensorimotor trajectory) and
harm-to-agency (obstruction of *another* agent's goal-pursuit) -- and that these need distinct
architectures. The claim's own implementation note lists "other-agent goal modelling (their
z_goal visible in shared state)" as prerequisite (a), and discriminant (1) as "what the other
agent's goal is." Woodward is the developmental grounding for exactly that prerequisite: it
shows that representing *what another agent is trying to do*, as a primitive separable from the
movement that realises it, is an early and robust competence in biological agents. The
separation Woodward demonstrates -- goal-object representation decoupled from the sensorimotor
path -- is the same architectural separation MECH-129 builds on: you cannot have a harm-to-agency
signal computed over another's goal unless that goal is represented independently of your own (or
their) physical trajectory.

The agency-gating finding has a second, sharper implication for the REE substrate. The infant
result is not a generic spatial-association mechanism -- it does not fire for inanimate movers.
That maps onto the `OTHER_SELFLIKE` / AGENCY-detector framing already in the project's empathy
notes (`docs/thoughts/2026-02-09_empathy.md`): a goal-interference signal in E3 must itself be
gated on an agency detector, or it will mistake passive environmental dynamics for thwarted
agents and generate spurious relational cost.

## Limitations and caveats

The honest boundary is that Woodward demonstrates goal *encoding*, not goal *obstruction*. It
grounds that the other's goal is represented (discriminant 1, prerequisite a); it says nothing
about whether interfering with that goal is registered as a cost -- which is the actual
harm-to-agency signal MECH-129 is about (discriminants 2-4 and the trajectory-pair interference
computation). So this paper supports the *substrate* of harm-to-agency, not the harm signal
itself. There is also the ordinary transfer risk: infant looking-time is a long way from a
computed interference signal in a multiagent REE environment, and a habituation dishabituation
contrast is evidence about representation, not about valuation. I have rated mapping fidelity 0.7
and transfer risk 0.4 to reflect that this is strong evidence for one necessary component and
silent on the rest. It earns "supports" because the component it grounds -- separable
goal-representation of another agent -- is genuinely load-bearing for MECH-129 and is exactly
what the claim names as its Level-3 prerequisite.

According to PubMed and the developmental-cognition literature, the canonical citation is
Woodward, A. L. (1998), *Cognition* 69(1):1-34,
[DOI 10.1016/S0010-0277(98)00058-4](https://doi.org/10.1016/S0010-0277(98)00058-4).
