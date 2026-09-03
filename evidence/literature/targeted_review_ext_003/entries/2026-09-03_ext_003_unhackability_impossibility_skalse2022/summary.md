# Unhackable proxies are essentially trivial (Skalse et al., NeurIPS 2022) — EXT-003

**Source:** Skalse J, Howe NHR, Krasheninnikov D, Krueger D. *Defining and Characterizing Reward Gaming*. Advances in Neural Information Processing Systems 35 (NeurIPS 2022), Main Conference Track. Preprint: arXiv:2209.13085, titled *Defining and Characterizing Reward Hacking* — same paper, retitled for the proceedings.

## What the paper does

The authors give reward hacking its first formal definition and then ask what it would take to avoid. A proxy reward is **unhackable** with respect to a true reward if increasing expected proxy return can *never* decrease expected true return. That is the property you would want any deployed reward function to have, and it is the property most reward-engineering intuitions implicitly assume is achievable with enough care. The paper's central result is that it usually is not. Over the set of all stochastic policies, two reward functions can be unhackable only if one of them is constant. The intuitive escape routes are closed off explicitly: making the reward "narrower" by omitting terms, or coarsening away distinctions between roughly equivalent outcomes, does not in general buy unhackability. The authors then restrict to deterministic policies and to finite sets of stochastic policies, where non-trivial unhackable pairs do exist, and characterise necessary and sufficient conditions for *simplifications*, an important special case.

## The finding that matters for EXT-003, and why it is stronger than the claim

EXT-003 has two halves. The premise is MECH-069's: sensory prediction error, motor-sensory error on `z_gamma`, and harm/goal error are incommensurable. The consequence is that collapsing them into one scalar *permits* credit misattribution, so an agent can satisfy the reward by optimising one channel at the expense of the others. This paper is the formal backing for the consequence — and it upgrades it. "Permits" is too weak a modality for what the theorem says. In the general stochastic-policy case, a non-constant scalar proxy is essentially always hackable; the question is not whether exploitable gaps exist but where they are and whether the agent is capable enough to find them (which is where Pan et al., also in this pull, picks up).

The mechanism the authors isolate is the one REE should care about: unhackability is such a strong condition *because* reward is linear in state-action visit counts. Linear aggregation is precisely the operation performed when three objectives are collapsed onto one scalar. ARC-021's answer — three separate cortico-striatal-like loops, each with its own error signal, its own optimiser, its own transition buffer — is a refusal to perform that aggregation at all. The architecture never forms the scalar whose optimisation the theorem indicts. The paper does not say anything about REE, obviously; what it supplies is the reason why declining to form that scalar is a principled move rather than merely a tidier engineering choice.

## Limitations, including one the entry should not smooth over

Three boundaries, and the second is the interesting one.

First, and most straightforwardly: the theorem is about a proxy/true reward *pair* in an MDP. It says nothing whatever about whether three particular error signals are mutually underivable. MECH-069's premise gets no support here. This entry evidences the consequence and is silent on the cause.

Second — and this is a tension I would rather state than bury — the paper's framing presupposes that there *is* a well-defined true reward function which the proxy imperfectly approximates. The strongest reading of EXT-003, and the reading MECH-069 actually licenses, is that no true scalar exists to be approximated at all, because the objectives are incommensurable. So this paper is an ally on the consequence while quietly assuming something the claim denies. That does not undermine its use here: if hacking is near-inevitable even in the *charitable* case where a true scalar exists, it is not better in the case where none does. But it does mean the paper is arguing for EXT-003's conclusion from a premise EXT-003 rejects, and a governance reader should know that.

Third, the negative result is proved over *all* stochastic policies. The authors are explicit that non-trivial unhackable pairs do exist once one restricts to deterministic policies or finite policy sets. It must not be quoted as an unconditional impossibility theorem.

## Confidence

0.78. Source quality is the highest in this pull (0.90) — NeurIPS main track, theorems with proofs, and a definitional framework that has since been widely adopted. Transfer risk is the lowest (0.22): there is no animal-to-human or simulation-to-deployment step to discount, because the result is a mathematical property of MDPs; the only residual is that REE's three-channel learning is not straightforwardly one MDP with one reward, so the theorem bites on the architecture REE rejects rather than on REE. Mapping fidelity (0.66) is the limiting term and is what holds the aggregate below the 0.85 band: the result targets EXT-003's consequence squarely and its premise not at all.
