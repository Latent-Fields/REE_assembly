# Da Costa, Parr, Sajid, Veselic, Neacsu & Friston (2020) — *Active inference on discrete state-spaces: A synthesis*

**Claims touched:** ARC-021 / MECH-069 (three incommensurable error channels), ARC-016 (multi-axis precision).
**Direction:** mixed — it *weakens* REE's "one scalar" objection as stated, and simultaneously *sharpens* the genuine departure REE can defend.

## Why this paper, not just the textbook

The Parr/Pezzulo/Friston textbook gives the prose; this synthesis gives the equations, and WS-5 turns on an equation-level distinction. The whole point of the workstream is that REE's rejection of active inference — "it collapses everything into a single free-energy functional" — is *partly a strawman*, and the only way to say exactly how partly is to look at what active inference actually optimises. This paper is the open-access, canonical place where that object is written down.

## What the math actually says

Two results are load-bearing for the bridge:

1. **Active inference optimises a *factorized* objective over a *factorized* state.** The approximate posterior is mean-field: `Q(s_1:T | π) = ∏_τ Q(s_τ | π)`, each factor a categorical distribution, with a further mean-field factorisation across *distinct hidden-state factors*. The generative model likewise factorises. So the claim that active inference "can only optimise one undifferentiated scalar" is simply false at the level of the formalism — it separates representational dimensions by construction.

2. **Expected free energy is a *sum* of separable value terms.** `G(π)` decomposes into extrinsic/pragmatic value (expected log preference — reward/utility, "the negative of Bayesian risk … when reward is log evidence") and intrinsic/epistemic value ("the expected information gain afforded by a particular policy, which can be about hidden states (i.e., salience) or model parameters (i.e., novelty)" — "it is this term that underwrites artificial curiosity"). Best policies minimise `G(π)`, giving behaviour that is at once risk-minimising and ambiguity-resolving.

Precision over policies (`γ`, with a Gamma prior) is "a plausible description of dopaminergic discharges" — a scalar gain on the softmax over policies.

## The strawman, dissolved — and the real departure, located

Put those two results next to REE's standing objection and the picture becomes precise:

- **The strawman half.** If REE's argument against active inference is "it forces one scalar," that argument is dead on arrival: the objective is factorized, the posterior is mean-field, and reward-seeking and information-seeking live in separate, named terms. REE gains nothing by attacking the number of scalars.

- **The real half — commensurability, not cardinality.** Every term of `G(π)` — risk and ambiguity, extrinsic and epistemic — is measured in **nats** and **added**. Active inference *assumes the value of information and the value of reward share a currency*. That is the assumption ARC-021/MECH-069 deny. REE's strong claim is that its three error channels (sensory-prediction, motor-sensory, harm/goal) have **no common currency**: forcing them through *any* shared scalar mis-attributes credit *even after* factorisation, because the errors are incommensurable in kind, not merely separable in index.

This reframing is the deliverable. REE is not rejecting a single objective (active inference has one and it is factorized); REE is rejecting a single *currency*. The V3-EXQ-009 evidence behind MECH-069 — wider E2 capacity produced overfitting rather than better harm attribution — is exactly the signature incommensurability predicts and commensurable-EFE does not: a single summed functional with enough parameters should eventually route harm credit correctly; an incommensurable-channel architecture predicts it *cannot, at any capacity*. That gives the falsifier: a forced-shared-loss ablation that fails to converge to correct credit assignment regardless of capacity supports MECH-069; one that succeeds with scale supports the commensurable-EFE null.

## ARC-016's multi-axis precision, in the same light

The precision object in this synthesis is a scalar / low-dimensional gain on a common surprise currency. It does not supply distinct, non-exchangeable precision axes. So ARC-016's *multi-axis* (heterogeneous) precision is not licensed by the standard formalism — it is an explicit enrichment REE proposes, and one it still owes a demonstration for: that single-currency precision cannot reproduce REE's mode transitions. Until then, multi-axis precision is a hypothesised extension of the (imported) active-inference precision lever, not a re-derivation of it.

## Confidence

0.61, mixed. High source quality (the definitive open-access mathematical synthesis, *Journal of Mathematical Psychology*). Mapping fidelity moderate: the factorisation and epistemic/extrinsic decomposition map cleanly onto the argument, but turning "commensurable-but-decomposed" into a concrete REE falsifier is interpretive. The paper's role is not to support MECH-069 — it is the precise null the strong claim must beat, and the reason the "one scalar" objection had to be restated as a "one currency" objection.
