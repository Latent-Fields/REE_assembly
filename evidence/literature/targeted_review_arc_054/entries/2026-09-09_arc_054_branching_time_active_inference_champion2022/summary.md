# Branching-time active inference: the objective form ARC-054 asserts is well-posed

**Claim tested:** ARC-054 (D_V trajectory selection over planning horizon H) · **Direction:** supports · **Confidence:** 0.60

## What the paper does

Champion and colleagues address a practical problem in active inference: expected free energy is defined over policies, and evaluating every policy over a horizon is intractable. Their move is to treat planning as structure learning over a *tree* of imagined futures, and to propagate expected free energy in two directions -- forward toward the leaves as the tree is expanded, and backward toward the root as values are aggregated. They show that the forward propagation corresponds to standard active inference and the backward to sophisticated inference, which clarifies a distinction that had been muddy, and they demonstrate that the resulting framework covers habit formation and curiosity as regimes of one objective rather than as bolt-on modules.

There is no biological data here. It is a formal contribution with supporting simulations.

## Why this bears on ARC-054

ARC-054 makes an unusual assertion for an architecture claim. It does not merely say "plan over a horizon"; it says the *objective* should be a discounted accumulation of an internally computed coherence quantity, J(pi) = sum over k of gamma^k times V_hat at t+k, and it makes the strong further claim that this *generalises* reward maximisation -- that reward becomes a special case of coherence preservation.

That is the kind of claim that can fail in two very different ways. It can fail empirically, by turning out to select worse. But it can also fail *formally*, by not being a well-posed objective at all, or by being well-posed and computationally hopeless. The second failure mode is the one this paper speaks to, and it speaks to it favourably. Accumulating a non-reward, internally-computed quantity across a discounted tree of imagined futures is well-posed; it can be computed by tree search with backward propagation from the leaves; and the agent that results recovers reward-seeking as one regime among several rather than needing reward bolted on separately. That last point is structurally the same generalisation relation ARC-054 asserts, arrived at independently in a different framework.

So this entry closes off the "the objective doesn't even make sense" objection. Given ARC-054's dependency chain and its V3 form's default-OFF status, that is worth having on the record.

## Where the mapping breaks, and I want to be precise about it

Expected free energy is not D_V. They share a *form* -- horizon-discounted accumulation of an internally computed quantity over imagined trajectories -- and they differ in *content*. EFE accumulates ambiguity plus risk relative to preferred outcomes. D_V, in ARC-054's V3 form, accumulates temporal-depth verisimilitude derived from MECH-269 per-region V_s, walked by the MECH-288 segmenter with a configurable EMA. Those are different quantities with different failure modes.

The consequence is that this paper evidences ARC-054's objective *form* and evidences nothing whatever about whether D_V is the right thing to put inside it. In particular it cannot discharge the claim's substantive assertion -- that optimising instantaneous V(t) alone creates short-term coherence traps and produces mania- or delusion-like failure modes. That assertion is the interesting part of ARC-054 and it remains untested by anything in this pull. It is a V3-EXQ-491 question.

A tractability caveat is also worth flagging as a live risk rather than a footnote. Tree search over EFE is exponential in horizon absent the paper's pruning strategy. If REE's H is long and its branching factor high, the tractability result may not transfer, and computing J(pi) could become the cost rather than the benefit -- a concrete engineering falsifier for the V3 form.

## Confidence reasoning

Source quality 0.72: rigorous, peer-reviewed in a solid venue, but a single-framework theoretical contribution whose validation is limited to simulations the authors chose. Mapping fidelity 0.65 for the form-matches-content-does-not situation above. Transfer risk is the lowest in this pull at 0.30, because this is computation-to-computation rather than biology-to-computation.

The aggregate of 0.60 is deliberately modest. A formal-possibility result is genuine support, but for an `arch_commitment` that asserts a *specific quantity* is the right one to optimise, showing that quantities of that general shape are optimisable is a fair distance from the claim.
