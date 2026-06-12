# Ng, Harada & Russell (1999) -- the formal tethering constraint on proxy goals

**Claim strand:** B (positive half) -- the condition under which an intermediate/proxy reward provably does NOT distort the true goal.
**Wires to:** INV-065 (proxy_goal_necessity) and the prospective candidate `proxy_tethering_guard`.

## Why this paper is the standout gap

REE's existing proxy-goal cluster (INV-065, MECH-216/217, ARC-051) establishes that a bounded-horizon planner *needs* intermediate proxy goals. None of REE's prior literature touches the dual question: when does optimizing a proxy *divert* the agent from the superordinate goal it was meant to serve? That is the alignment/Goodhart question, and it lives in the ML literature REE's neuroscience-heavy pulls had not reached. This paper is the foundational positive result.

## What it proves

Ng et al. ask which additive modifications to a reward function leave the *set of optimal policies* unchanged. **Theorem 1:** a shaping reward F is guaranteed to preserve the optimal policy **if and only if** it is *potential-based* -- i.e. there is a state-potential function Phi with

  F(s, a, s') = gamma * Phi(s') - Phi(s).

The "only if" is the strong, load-bearing half: if F is *not* of this form, there exist transition dynamics and a base reward under which the shaped problem's optimal policy differs from the true one. Sufficiency holds with **no assumptions on the dynamics or base reward** -- the dynamics-independence is what makes it foundational. Under a potential-based F the optimal action-values shift by exactly the potential, Q'(s,a) = Q(s,a) - Phi(s), so the arg-max over actions is untouched.

## The mapping to REE

This is the tethering constraint Daniel's "what am I missing" was pointing at. A proxy/progress signal that maintains a goal is the same machinery that can let an agent drift -- *unless* the proxy has the potential-difference structure. The clean REE translation: a maintenance proxy defined as a difference of a goal-proximity potential is alignment-safe by construction; an arbitrary learned or affective bonus is not. That grounds a candidate `proxy_tethering_guard` claim as a child of INV-065 -- the proxy must approximate a potential over goal-proximity to serve the superordinate goal rather than supplant it.

## The honest caveat

The guarantee is exact only for a stationary, additive, *state-only* potential under a fixed discount. REE's maintenance proxy is learned online, non-stationary, and affectively modulated -- precisely the cases that break the theorem unless handled with the later dynamic-potential machinery. So this transfers as a *design target* and a *limiting-case certificate*, not as an off-the-shelf guarantee. The direction is therefore `mixed`: it supports the usefulness of intermediate signals while proving an untethered proxy can divert the agent.
